from django.urls import path
from .views import signup,logoutview,loginview


urlpatterns=[
    path('signup/',signup,name="signup"),
    path('logout/',logoutview,name="logout"),
    path('login/',loginview,name="login")

]