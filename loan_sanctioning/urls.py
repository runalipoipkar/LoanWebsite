
from django.urls import path
from .views import LoanViewSet

urlpatterns=[
    path('loan/',LoanViewSet.as_view({'get':'list','post':'create'})),
    path('loan/<int:pk>/',LoanViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'}))
]