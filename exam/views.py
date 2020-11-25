from django.shortcuts import render
from django.core.mail import send_mail
from .models import *
import math,random
from django.http import HttpResponse,JsonResponse
from rest_framework.decorators import api_view
from django.contrib.auth.models import User
from rest_framework.views import APIView 
from rest_framework.response import Response 
from rest_framework.permissions import IsAuthenticated,AllowAny
from datetime import datetime
class addqn(APIView): 
    permission_classes = (IsAuthenticated, ) 
    def post(self, request): 
        x=request.data
        w=str(datetime.now().timestamp()*1000000)
        questions1(w,x['question'],x['options'],x['ans']).save()
        return JsonResponse({'result':w})
class addtest(APIView): 
    permission_classes = (IsAuthenticated, ) 
    def get(self,request):
        x=request.data
        l=[]
        w=test1.objects.all()
        for i in w:
            l.append(i.getv())
        return JsonResponse({'result':l})
    def post(self, request): 
        x=request.data
        w=str(datetime.now().timestamp()*1000000)
        test1(w,x['theme'],x['desc'],x['noofstd'],x['start'],x['end'],x['qns']).save()
        return JsonResponse({'result':w})