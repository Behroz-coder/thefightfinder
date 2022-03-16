from multiprocessing import context
from queue import Empty
from tokenize import blank_re
from django.shortcuts import redirect, render
from events.models import *
from UserInformation.models import *
from django.conf import settings
import json
from urllib.parse import urlparse
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from seminar.models import *
# Create your views here.


def index(request):
    user = User.objects.filter(username=request.user)
    context = {}
    if(user.count()):
        userinfo = UserInformation.objects.filter(name=user[0])

        user_type = True
        if str(userinfo[0].type) == 'Martial Artist':
            user_type = False
        context['user_type'] = user_type
    return render(request, "index.html", context)
    # return render(request, "index.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, "UserName or Password Invalid.")
            return redirect('login_view')
    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect("login_view")


def email(request, email):
    if request.method == "GET":
        message = ''
        if User.objects.filter(email=email).exists():
            message = '* Email already exists.'

        return JsonResponse({'success': message})


def username(request, username):
    if request.method == "GET":
        message = ''
        if User.objects.filter(username=username).exists():
            message = '* Username already exists.'

        return JsonResponse({'success': message})


def signup(request):
    usertype = UserType.objects.all()
    if(request.method == "POST"):
        usertype = request.POST.get('usertype')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cpassword = request.POST.get('cpassword')
        # print(usertype)
        utype = UserType.objects.get(id=usertype)
        if password == cpassword:
            user = User.objects.create_user(username, email, password)
            user.first_name = firstname
            user.last_name = lastname
            user.save()
            userinfo = UserInformation.objects.create(type=utype, name=user)
            userinfo.save()
            message = 'Account Created Successfully.'
            messages.success(
                request, "You have registered successfully, now login!")
            return redirect("login_view")

    return render(request, "signup.html", {'usertype': usertype})


def search(request):
    events = Event.objects.all()
    e_arry = []
    for e in events:
        e_arry.append(
            {
                "cords": {
                    "lat": e.event_Location.latitude,
                    "lng": e.event_Location.longitude,
                },
                "title": e.title,
            }
        )
    print(json.dumps(e_arry))
    context = {
        "apikey": settings.MAP_API_KEY,
        "events": e_arry,
    }
    user = User.objects.filter(username=request.user)

    if(user.count()):
        userinfo = UserInformation.objects.filter(name=user[0])

        user_type = True
        if str(userinfo[0].type) == 'Martial Artist':
            user_type = False
        context['user_type'] = user_type
    return render(request, "search_event.html", context)


def news(request):
    user = User.objects.filter(username=request.user)
    context = {}
    if(user.count()):
        userinfo = UserInformation.objects.filter(name=user[0])

        user_type = True
        if str(userinfo[0].type) == 'Martial Artist':
            user_type = False
        context['user_type'] = user_type
    allnews = New.objects.all()
    context['newslist'] = allnews
    return render(request, "news.html", context)


def news_page(request, slug):
    user = User.objects.filter(username=request.user)
    context = {}
    if(user.count()):
        userinfo = UserInformation.objects.filter(name=user[0])

        user_type = True
        if str(userinfo[0].type) == 'Martial Artist':
            user_type = False
        context['user_type'] = user_type

    news = New.objects.filter(slug=slug)[0]
    context['news'] = news

    return render(request, "news_page.html", context)


def about(request):
    user = User.objects.filter(username=request.user)
    context = {}
    if(user.count()):
        userinfo = UserInformation.objects.filter(name=user[0])

        user_type = True
        if str(userinfo[0].type) == 'Martial Artist':
            user_type = False
        context['user_type'] = user_type

    return render(request, "about_us.html", context)


def dashboard(request):
    user = User.objects.filter(username=request.user)
    context = {}
    if(user.count()):
        userinfo = UserInformation.objects.filter(name=user[0])

        user_type = True
        if str(userinfo[0].type) == 'Martial Artist':
            user_type = False
        context['user_type'] = user_type
    events = Events.objects.all()
    context['events'] = events

    return render(request, "dashboard.html", context)


def delete_event(request, id):
    event = Events.objects.filter(id=id)
    if event:
        event[0].delete()
        messages.success(
            request, "Event Delete Successfully.")
    return redirect("dashboard")


def edit_event(request, id):
    event = Events.objects.filter(id=id)
    user = User.objects.filter(username=request.user)
    context = {}

    if user:
        userinfo = UserInformation.objects.filter(name=user[0])

        user_type = True
        if str(userinfo[0].type) == 'Martial Artist':
            user_type = False
        context['user_type'] = user_type

    if event:
        if(request.method == "POST"):
            e = event[0]
            e.event_name = request.POST.get('event_name')
            e.event_organizer = request.POST.get('event_organizer')
            e.event_date = request.POST.get('event_date')
            e.organizer_contact_number = request.POST.get(
                'organizer_contact_number')
            e.event_address = request.POST.get('event_address')
            e.organizer_contact_email = request.POST.get(
                'organizer_contact_email')
            e.event_cost = request.POST.get('event_cost')
            e.event_website = request.POST.get('event_website')
            event_style = request.POST.get('event_style')
            competition_type = request.POST.get('competition_type')
            e.event_social_links_fb = request.POST.get('event_social_links_fb')
            e.event_social_links_tw = request.POST.get('event_social_links_tw')
            e.organizer_social_links_fb = request.POST.get(
                'organizer_social_links_fb')
            e.organizer_social_links_tw = request.POST.get(
                'organizer_social_links_tw')
            e.event_rules_requlations = request.POST.get(
                'event_rules_requlations')
            e.special_request_form_event_organizer = request.POST.get(
                'special_request_form_event_organizer')
            if event_style == "":
                e.event_style = None
            else:
                e.event_style = Event_style.objects.get(style=event_style)

            if competition_type == "":
                e.competition_type = None
            else:
                e.competition_type = Competition_type.objects.get(
                    type=competition_type)

            e.save()
            messages.success(
                request, "Event Update Successfully.")
            return redirect("dashboard")

        context['edit_event'] = event[0]

        event_style = Event_style.objects.all()
        context['event_style'] = event_style
        competition_type = Competition_type.objects.all()
        context['competition_type'] = competition_type
        return render(request, "edit_event.html", context)
    else:
        return redirect("dashboard")


def add_event(request):
    user = User.objects.filter(username=request.user)
    context = {}

    if(user.count()):
        userinfo = UserInformation.objects.filter(name=user[0])

        user_type = True
        if str(userinfo[0].type) == 'Martial Artist':
            user_type = False
        context['user_type'] = user_type

    event_style = Event_style.objects.all()
    context['event_style'] = event_style
    competition_type = Competition_type.objects.all()
    context['competition_type'] = competition_type
    if(request.method == "POST"):
        print(request.POST)
        event_name = request.POST.get('event_name')
        event_organizer = request.POST.get('event_organizer')
        event_date = request.POST.get('event_date')
        organizer_contact_number = request.POST.get('organizer_contact_number')
        event_address = request.POST.get('event_address')
        organizer_contact_email = request.POST.get('organizer_contact_email')
        event_cost = request.POST.get('event_cost')
        event_website = request.POST.get('event_website')
        event_style = request.POST.get('event_style')
        competition_type = request.POST.get('competition_type')
        event_social_links_fb = request.POST.get('event_social_links_fb')
        event_social_links_tw = request.POST.get('event_social_links_tw')
        organizer_social_links_fb = request.POST.get(
            'organizer_social_links_fb')
        organizer_social_links_tw = request.POST.get(
            'organizer_social_links_tw')
        event_rules_requlations = request.POST.get('event_rules_requlations')
        special_request_form_event_organizer = request.POST.get(
            'special_request_form_event_organizer')
        if event_style == "":
            event_style = None
        else:
            event_style = Event_style.objects.get(style=event_style)

        if competition_type == "":
            competition_type = None
        else:
            competition_type = Competition_type.objects.get(
                type=competition_type)

        event = Events(
            event_name=event_name,
            event_organizer=event_organizer,
            event_date=event_date,
            organizer_contact_number=organizer_contact_number,
            event_address=event_address,
            organizer_contact_email=organizer_contact_email,
            event_cost=event_cost,
            event_website=event_website,
            event_style=event_style,
            competition_type=competition_type,
            event_social_links_fb=event_social_links_fb,
            event_social_links_tw=event_social_links_tw,
            organizer_social_links_fb=organizer_social_links_fb,
            organizer_social_links_tw=organizer_social_links_tw,
            event_rules_requlations=event_rules_requlations,
            special_request_form_event_organizer=special_request_form_event_organizer,
        )
        event.save()
        messages.success(
            request, "Event Saved Successfully.")
        return redirect("dashboard")

    return render(request, "add_event.html", context)


def add_seminar(request):
    user = User.objects.filter(username=request.user)
    context = {}
    if(user.count()):
        userinfo = UserInformation.objects.filter(name=user[0])

        user_type = True
        if str(userinfo[0].type) == 'Martial Artist':
            user_type = False
        context['user_type'] = user_type

    event_style = Event_style.objects.all()
    context['event_style'] = event_style
    competition_type = Competition_type.objects.all()
    context['competition_type'] = competition_type
    if(request.method == "POST"):
        print(request.POST)
        seminar_name = request.POST.get('seminar_name')
        seminar_organizer = request.POST.get('seminar_organizer')
        seminar_date = request.POST.get('seminar_date')
        organizer_contact_number = request.POST.get('organizer_contact_number')
        seminar_address = request.POST.get('seminar_address')
        organizer_contact_email = request.POST.get('organizer_contact_email')
        seminar_cost = request.POST.get('seminar_cost')
        seminar_website = request.POST.get('seminar_website')
        seminar_style = request.POST.get('seminar_style')
        competition_type = request.POST.get('competition_type')
        seminar_social_links_fb = request.POST.get('seminar_social_links_fb')
        seminar_social_links_tw = request.POST.get('seminar_social_links_tw')
        organizer_social_links_fb = request.POST.get(
            'organizer_social_links_fb')
        organizer_social_links_tw = request.POST.get(
            'organizer_social_links_tw')
        seminar_rules_regulations = request.POST.get(
            'seminar_rules_regulations')
        special_request_form_seminar_organizer = request.POST.get(
            'special_request_form_seminar_organizer')
        if seminar_style == "":
            seminar_style = None
        else:
            seminar_style = Event_style.objects.get(style=seminar_style)

        if competition_type == "":
            competition_type = None
        else:
            competition_type = Competition_type.objects.get(
                type=competition_type)

        # event = Seminar(
        #     seminar_name=seminar_name,
        #     seminar_organizer=seminar_organizer,
        #     seminar_date=seminar_date,
        #     organizer_contact_number=organizer_contact_number,
        #     seminar_address=seminar_address,
        #     organizer_contact_email=organizer_contact_email,
        #     seminar_cost=seminar_cost,
        #     seminar_website=seminar_website,
        #     seminar_style=seminar_style,
        #     competition_type=competition_type,
        #     seminar_social_links_fb=seminar_social_links_fb,
        #     seminar_social_links_tw=seminar_social_links_tw,
        #     organizer_social_links_fb=organizer_social_links_fb,
        #     organizer_social_links_tw=organizer_social_links_tw,
        #     seminar_rules_regulations=seminar_rules_regulations,
        #     special_request_form_seminar_organizer=special_request_form_seminar_organizer
        # )
        # event.save()
        messages.success(
            request, "Seminar Saved Successfully.")
        return redirect("dashboard")

    return render(request, "add_seminar.html", context)


def add_school(request):
    user = User.objects.filter(username=request.user)
    context = {}
    if(user.count()):
        userinfo = UserInformation.objects.filter(name=user[0])

        user_type = True
        if str(userinfo[0].type) == 'Martial Artist':
            user_type = False
        context['user_type'] = user_type

    return render(request, "add_school.html", context)


def user_profile(request):
    user = User.objects.filter(username=request.user)
    context = {}
    if(user.count()):
        userinfo = UserInformation.objects.filter(name=user[0])

        user_type = True
        if str(userinfo[0].type) == 'Martial Artist':
            user_type = False
        context['user_type'] = user_type
    return render(request, "user_profile.html", context)


def reviews(request):
    user = User.objects.filter(username=request.user)
    context = {}
    if(user.count()):
        userinfo = UserInformation.objects.filter(name=user[0])

        user_type = True
        if str(userinfo[0].type) == 'Martial Artist':
            user_type = False
        context['user_type'] = user_type

    players = Player.objects.all()
    context["players"] = players

    return render(request, "reviews.html", context)


def review_page(request, slug):

    player = Player.objects.filter(slug=slug)[0]
    a = []
    a.append(player.num_1star)
    a.append(player.num_2star)
    a.append(player.num_3star)
    a.append(player.num_4star)
    a.append(player.num_5star)
    maxv = max(a)
    s1 = a[0]/maxv*100
    s2 = a[1]/maxv*100
    s3 = a[2]/maxv*100
    s4 = a[3]/maxv*100
    s5 = a[4]/maxv*100
    context = {
        "player": player,
        "1star":  s1,
        "2star":  s2,
        "3star":  s3,
        "4star":  s4,
        "5star":  s5,
        "maxr": ['s', 's', 's', 's', 's']
    }
    user = User.objects.filter(username=request.user)

    if(user.count()):
        userinfo = UserInformation.objects.filter(name=user[0])

        user_type = True
        if str(userinfo[0].type) == 'Martial Artist':
            user_type = False
        context['user_type'] = user_type

    return render(request, "review_page.html", context)
