from django.shortcuts import render
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from collections import namedtuple
import json

# Create your views here.
from django.http import HttpResponse, JsonResponse


def sendTempHumData(request):
    if request.method == 'GET':
        temperature = request.GET.get("temperature", False)
        humidity = request.GET.get("humidity", False)

        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "INSERT INTO mydata(tempData, humidity) VALUES ('"+str(temperature) + "','"+str(humidity) + "' )")
    return HttpResponse("Hello, world. You're at the polls index.")

