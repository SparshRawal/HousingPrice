from django.contrib import admin
from django.urls import path, include
from pricePrediction.views import predict_price
from pricePrediction.forms import HouseFeaturesForm

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include('djoser.urls')),
    path('predictPrice/', predict_price, name='predict_price'),
]
