
from django.urls import path,re_path
from varcons import views





urlpatterns = [
   
    path('homepage/', views.homepage,name="homepage"),


    path('subscribe/', views.subscribe),
    path('', views.home),
  
   
   
    path('contactus/', views.contactus),
    path('courses/', views.courses),
    path('quiz/', views.quiz),
    path('quizhin/', views.quizhin),
    path('quizeng/', views.quizeng),
    path('quizkan/', views.quizkan),
   
    path('login1/', views.login1),
    path('kannada/', views.kannada),
    path('English/', views.English),
    path('Hindi/', views.Hindi),
    path('translate/', views.translate),
    path('signup/',views.signup)


   
]
