from django.shortcuts import render
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from collections import namedtuple
import json

# Create your views here.
from django.http import HttpResponse, JsonResponse

@csrf_exempt
def writelocation(request):
    if request.method == 'GET':
        botNumber = "1"
        Locationo = request.GET.get("Locationo", False)
        Status = request.GET.get("Status", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "INSERT INTO bot_location(botNumber, Location, Status) VALUES ('"+str(botNumber) + "','" + str(Locationo) + "','" + str(Status) + "' )")
            connection.close()
        return HttpResponse()

@csrf_exempt
def controlCar(request):
    if request.method == 'POST':
        with connection.cursor() as cursor_1:
            cursor_1.execute("SELECT * from bot_location")
            row1 = cursor_1.fetchone()
        if row1 == None:
            pass
        else:
            status = request.POST.get("status", False)
            botNumber = "1"
            if status == "Start":
                with connection.cursor() as cursor_1:
                    cursor_1.execute(
                        "update bot_location set Status='" + str(status) + "' where botNumber = '"+ str(botNumber) + "'")
                    connection.close()
            else:
                with connection.cursor() as cursor_1:
                    cursor_1.execute(
                        "update bot_location set Status='" + str(status) + "' where botNumber = '"+ str(botNumber) + "'")
                    connection.close()
    return HttpResponse()

@csrf_exempt
def readStatus(request):
    if request.method == 'GET':
        with connection.cursor() as cursor_1:
            cursor_1.execute("SELECT Status from bot_location order by Serial DESC LIMIT 1")
            row1 = cursor_1.fetchone()
            connection.close()
            if row1 == None:
                return HttpResponse("", content_type="application/json")
            else:
                response_data = {}
                response_data['result'] = row1[0]
                json_data = json.dumps(response_data)
                return HttpResponse(json_data, content_type="application/json")
    return HttpResponse()
        
