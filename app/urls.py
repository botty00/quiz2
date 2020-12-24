from django.urls import path
from . import views

urlpatterns = [  
   path('create_user',views.create_user,name='create_user'),
   path('loginview',views.loginview,name='loginview'),
   path('question1',views.question1,name='question1'),
   path('question2',views.question2,name='question2'),
   path('question3',views.question3,name='question3'),
   path('answer/<int:correct>',views.answer,name='answer'),
   path('answer2/<int:correct>',views.answer2,name='answer2'),
   path('answer3/<int:correct>',views.answer3,name='answer3'),
   path('result',views.result,name='result'),
   path('start',views.start,name='start'),
   path('top',views.top,name='top'),
   path('complete',views.complete,name='complete'),
   path('logoutview',views.logoutview,name='logoutview'),
   path('rank',views.rank,name='rank'),
   path('rank2',views.rank2,name='rank2'),
   path('rank3',views.rank3,name='rank3'),
]
