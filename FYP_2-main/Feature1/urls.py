from django.urls import path
from . import views

urlpatterns=[
    path('error/',views.handle_404,name="error"),
    path('home/',views.index,name="index"),
    path('',views.index,name="index"),
    path('login/',views.login,name="login"),
    path('signup/',views.signup,name="signup"),
    path('choose/',views.choose_user_type,name="choose_user_type"),
    path('lawyer_list',views.lawyer_list,name="lawyer_list"),
    path('contact',views.contact,name="contact"),
    path('about',views.help,name="help"),
    path('editprofile',views.editprofile,name="editprofile"),


    path('Lawyer/<num>/',views.lawyer, name="num"),
    path('my_profile',views.my_profile,name="my_profile"),
    path('createfile',views.create_file,name="create_file"),
    # path('recommended_lawyers',views.recommended_lawyers,name="recommended_lawyers"),

    path('Lawyer/<num>/connect',views.lawyerconnect, name="num"),
    

    path('Lawyer/connectClient',views.connectClient,name="connectClient"),
    path('pastcases/',views.PastCases,name="PastCases"),
    path('acceptedCases/',views.acceptedCases,name="acceptedCases"),
    path('casestatus',views.casestatus,name="casestatus"),
    # path('computation/<name>',views.computation, name="name"),
]