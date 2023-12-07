import time
import requests

from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status

from .models import Challenger

from .serializers import ChellangerSerializer


class ReportView(APIView):
    def post(self, request: Request) -> Response:
        pass
