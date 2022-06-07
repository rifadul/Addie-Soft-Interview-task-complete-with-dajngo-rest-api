
from django.contrib import admin
from django.urls import path,include
from api.views import SalesViewSet,ProductViewSet,SalesDetailsViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()

router.register('sales',SalesViewSet,basename = 'sales')
router.register('product',ProductViewSet,basename = 'product')
router.register('salesDetails',SalesDetailsViewSet,basename = 'salesDetails')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls'))
]
