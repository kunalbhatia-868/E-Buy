from django.urls import path
from .views import signup,logoutview,loginview,uniqueUsername


urlpatterns=[
    path('signup/',signup,name="signup"),
    path('logout/',logoutview,name="logout"),
    path('login/',loginview,name="login")
]

htmx_url_patterns=[
    path('check-username/',uniqueUsername)
]


urlpatterns+=htmx_url_patterns