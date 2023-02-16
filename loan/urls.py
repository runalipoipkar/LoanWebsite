from django.contrib import admin
from django.urls import path,include
#from rest_framework.routers import DefaultRouter
#from application_app.views import ApplicationAPI
#from disburstment.views import VendorViewSet,InstallmentViewSet,DisbursementViewSet
#from loan_sanctioning.views import LoanAPI
#from Admin_app.views import UserAPI

'''
router=DefaultRouter()
router.register('loan',LoanAPI,basename='loan')
router.register('vendor',VendorViewSet,basename='vendor')
router.register('installment',InstallmentViewSet,basename='installment')
router.register('application',ApplicationAPI,'application')
#router.register('user',UserAPI,basename='user')
router.register('disbursement',DisbursementViewSet,basename='disbursement')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('pro/', include('Admin_app.urls'))
]
'''


urlpatterns = [
    path('admin/', admin.site.urls),
    path('admin_app/',include("Admin_app.urls")),
    path('apps/',include("application_app.urls")),
    path('dis/',include("disburstment.urls")),
    path('l/',include("loan_sanctioning.urls"))
    #path("api/",include(router.urls))
]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)

