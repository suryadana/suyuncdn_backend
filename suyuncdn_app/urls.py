from django.urls import path
from suyuncdn_app.views import CountryListAPIView, CountryUpdateAPIView

urlpatterns = [
   path('country/', CountryListAPIView.as_view(), name='list'),
   path('country/update/', CountryUpdateAPIView.as_view(), name='update'),
]
