from rest_framework import generics, permissions
from rest_framework.response import Response

from suyuncdn_app.serializer import (
    Country, CountrySerializer,
    CountryUpdateSerialiser
)

# Create your views here.

class CountryListAPIView(generics.ListAPIView):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    permission_class = (permissions.AllowAny,)


class CountryUpdateAPIView(generics.GenericAPIView):
    queryset = Country.objects.all()
    serializer_class = CountryUpdateSerialiser
    permission_class = (permissions.AllowAny,)

    def patch(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        Country.objects.filter(id__in=serializer.validated_data['countries']).update(is_banned=True)
        Country.objects.exclude(id__in=serializer.validated_data['countries']).update(is_banned=False)
        return Response(serializer.data)
