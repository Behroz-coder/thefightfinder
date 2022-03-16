from django.urls import path
from tffsite.views import *

urlpatterns = [
    path('', index, name='index'),
    path('search/', search, name='search'),
    path('news/', news, name='news'),
    path('news/<slug>/', news_page, name='news_page'),
    path('about/', about, name='about'),
    path('profile/', user_profile, name='profile'),
    path('reviews/', reviews, name='reviews'),
    path('reviews/<slug>/', review_page, name='review_page'),
    path('email/<str:email>/', email, name='email'),
    path('username/<str:username>/', username, name='username'),
    path('login/', login_view, name='login_view'),
    path('logout/', logout_view, name='logout_view'),
    path('signup/', signup, name='signup'),


    path('dashboard/', dashboard, name='dashboard'),
    path('dashboard/add-event/', add_event, name='add_event'),
    path('dashboard/edit-event/<int:id>/', edit_event, name='edit_event'),
    path('dashboard/delete-event/<int:id>/',
         delete_event, name='delete_event'),
    path('dashboard/add-seminar/', add_seminar, name='add_seminar'),
    path('dashboard/add-school/', add_school, name='add_school'),

]
