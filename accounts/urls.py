
from django.urls import path
from . import views 



urlpatterns = [

    path('register/',views.registerPage, name="register"),
    path('login/',views.loginPage, name="login"),
    path('logout/',views.logoutUser, name="logout"),
    path('',views.home, name="home"),
    path('adminPage/',views.adminPage, name="adminPage"),

    path('landingPage/',views.landingPage , name="landingPage"),
   
    path("upload",views.send_files,name="uploads"),

    path("upload2",views.send_files2,name="uploads2"),

    path("adminPage",views.adminPage,name="adminPage"),

    #path("upload/<int:pk>",views.delete,name="deletef")


  
   
 
]
