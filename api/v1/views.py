from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from leads import models as m
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser

from . import serializers as s
from .sqs import LeadQueue


class LeadCreate(generics.CreateAPIView):
    queryset = m.Leads.objects.all()
    serializer_class = s.LeadSerializer
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        data = request.data

        serializer = self.serializer_class(data=data, many=False)
        if serializer.is_valid():
            name = serializer.validated_data["name"]
            email = serializer.validated_data["email"]
            subject = serializer.validated_data["subject"]
            message = serializer.validated_data["message"]
            lead = LeadQueue(name, email, subject, message)
            lead.queue()
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)


class StatusView(APIView):
    """
    Status
    """

    def get(self, request):
        return Response("ok")

class FailView(APIView):
    """
    Fail
    """

    def get(self, request):
        import sys
        sys.exit(-128)
