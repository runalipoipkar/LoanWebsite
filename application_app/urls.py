
from django.urls import path
from .views import ApplicationViewSet

urlpatterns=[
    path('application/',ApplicationViewSet.as_view({'get':'list','post':'create'})),
    path('application/<int:pk>/',ApplicationViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}))
]
