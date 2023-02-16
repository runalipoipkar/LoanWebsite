

from django.urls import path
from .views import DisbursementViewSet,VendorViewSet,InstallmentViewSet,send_new_mail

urlpatterns=[
    path('disbursement/',DisbursementViewSet.as_view({'get':'list','post':'create'})),
    path('disbursement/<int:pk>/',DisbursementViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('vendor/',VendorViewSet.as_view({'get':'list','post':'create'})),
    path('vendor/<int:pk>/',VendorViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('installment/',InstallmentViewSet.as_view({'get':'list','post':'create'})),
    path('installment/<int:pk>/',InstallmentViewSet.as_view({'get':'retrieve','put':'update','delete':'destroy'})),
    path('dismail/<int:pk>/', send_new_mail)
]