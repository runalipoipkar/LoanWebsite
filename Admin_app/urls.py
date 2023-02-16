from django.urls import path
#from .views import UserView
from .views import *
'''
urlpatterns=[
    path('user/',UserAPI.as_view()),
    path('user/<int:pk>/',UserDetailsAPI.as_view())

]
'''

urlpatterns=[
    path('user/',UserView.as_view({'get':'list','post':'create'})),
    path('user/<int:pk>/',UserView.as_view({'get':'retrieve','put':'update','delete':'destroy'}))
]

