from django.shortcuts import render
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .serializers import CitizenSerializer


class CNVList(ListAPIView):
    serializer_class = CitizenSerializer
    model = serializer_class.Meta.model
    paginate_by = 100

    def get_queryset(self):
        queryset = self.model.objects.all()
        return queryset.order_by('-FECHA_NACIDO')
