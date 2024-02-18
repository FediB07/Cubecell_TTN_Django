from rest_framework import viewsets

from ..models import Data
from .serializers import ModelSerializer


class ViewSet(viewsets.ModelViewSet):
    queryset=Data.objects.all()
    serializer_class = ModelSerializer