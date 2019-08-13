from django.shortcuts import render
from rest_framework import status, permissions
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView
import traceback, time

# Create your views here.
class Data(APIView):

    permission_classes = (AllowAny,)

    def get(self, req):
        m = {
            'data': [1, 2, 3],
            'name': 'test-data'
        }
        return Response(m)

class SecureData(APIView):

    def get(self, req):
        ls = ['test1', 'test2']
        return Response(ls)

class DelayData(APIView):

    def get(self, req):
        time.sleep(20)
        return Response({ 'ok': 1 })

class UserDetail(APIView):

    def get(self, req):
        user = req.user
        m = {
            'username': user.username,
            'groups': [
                {
                    'id': x.id,
                    'name': x.name
                } for x in user.groups.all()
            ]
        }
        return Response(m)