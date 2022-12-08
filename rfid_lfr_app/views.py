from django.shortcuts import render
from django.db import connection
from django.views.decorators.csrf import csrf_exempt
from collections import namedtuple
import json

# Create your views here.
from django.http import HttpResponse, JsonResponse


def writelocation(request):
    if request.method == 'GET':
        Location = request.GET.get("Location", False)
        with connection.cursor() as cursor_1:
            cursor_1.execute(
                "INSERT INTO bot_location(Location) VALUES ('"+str(Location) + "' )")
    return HttpResponse("Hello, world. You're at the polls index.")

def readlocation(request):
    if request.method == 'GET':
        with connection.cursor() as cursor_1:
            cursor_1.execute("select Serial, Location from bot_location")
            row1 = cursor_1.fetchall()
            result = []
            keys = ('Serial', 'Location')
            for row in row1:
                result.append(dict(zip(keys, row)))
            json_data = json.dumps(result)
            return HttpResponse(json_data, content_type="application/json")


