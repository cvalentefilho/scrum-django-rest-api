from rest_framework import viewsets

from .models import Sprint
from .serializers import SprintSerializer


class SprintViewsSet(viewsets.ModelViewSet):

    """Endpoint da API para listar e criar sprints."""

    queryset = Sprint.objects.order_by('end')
    serializer_class = SprintSerializer
