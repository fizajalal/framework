from django.urls import path
from profiles import views

urlpatterns = [
    # path('profile/', views.profile, name='profile'),
    path('signup',views.signup,name='signup'),
    path('',views.signin,name='signin'),
    path('signin',views.signin,name='signin'),
    path('home',views.home,name='home'),
    path('add_work',views.add_work,name='add_work'),


]

