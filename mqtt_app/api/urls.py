from rest_framework import routers

from django.urls import include, path

from .views import ViewSet

router = routers.DefaultRouter()
router.register(r'Data',ViewSet)

urlpatterns = [
    path('',include(router.urls))
]