from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
import requests
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from foo.models import Employees,Mobile2,Pingresults,AdExtractor
from django.contrib.auth.models import User





# Create your views here.
def view(request):
    return HttpResponse('i am inn goo')

class PingApiView(APIView):
    authentication_classes = []
    permission_classes = []
    status_code=requests.codes.ok


    def post(self, request):
        response = {"status_code": self.status_code}
        sessionkey=request.session.session_key
        print("Sessionkey",sessionkey)
        request_data = request.data
        print(request_data)
        response['activity_id']="12345"
        b=request.data['hostname']

        print(b)
        x=request.META
        print(x)

        Pingresults.objects.create(hostname=b)


        return Response(response, status=self.status_code)


class AdExtractorApiView(APIView):
    authentication_classes = []
    permission_classes = []
    status_code=requests.codes.ok


    def post(self, request):
        response = {"status_code": self.status_code}
        sessionkey=request.session.session_key
        print("Sessionkey",sessionkey)
        response["sessionkey"] = sessionkey
        request_data = request.data
        print(request_data)
        response['activity_id']="12345"

        b=request.data['hostname']

        print(b)
        x=request.META
        print(x)

        AdExtractor.objects.create(Hostname=b)
        return Response(response, status=self.status_code)
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.status import (
    HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND,
    HTTP_200_OK
)
from rest_framework.response import Response


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    return Response({'token': token.key},
                    status=HTTP_200_OK)
