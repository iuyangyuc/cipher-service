from django.urls import path
from .views import greeting, encoderendpoint

urlpatterns = [
    path("", greeting),
    path("docipher/<str:text>/<int:shift>", encoderendpoint)
]
