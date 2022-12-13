from django.contrib import admin
from django.urls import path, include
from ecommerce.drf.views import CategoryList, ProductList, ProductInventoryByWebId

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path("api/inventory/category/all/", CategoryList.as_view(),),
    path("api/inventory/products/category/<str:query>/", ProductList.as_view(),),
    path("api/inventory/<int:query>/", ProductInventoryByWebId.as_view(),),
]
