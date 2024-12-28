from django.urls import path
from .views import HomePageView, BasePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('base/', BasePageView.as_view(), name='base'),
]