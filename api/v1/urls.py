from django.urls import include, path
from rest_framework import routers

from . import views as v

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', v.StatusView.as_view()),
    path('leads/', v.LeadCreate.as_view()),
    path('fail/', v.FailView.as_view()),
    path('hola/', v.FailView.as_view())
]
