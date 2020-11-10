from django.urls import path, include

from rest_framework import routers, serializers

from leads import models as m
# Serializers define the API representation.


class LeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = m.Leads
        fields = "__all__"
