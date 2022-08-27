from django.shortcuts import render

from measurements.models import Measurement

from .logic import measurements_logic as ms
from measurements.logic.measurements_logic import get_measurements
from django.http import HttpResponse
from django.core import serializers
import json
from django.views.decorators.csrf import csrf_exempt

def measurements_view(request):
    if request.method == 'GET':
        id = request.GET.get("id", None)
        if id:
            measurement_dto = ms.get_measurement(id)
            measurement = serializers.serialize('json', [measurement_dto,])
            return HttpResponse(measurement, 'application/json')
        else:
            measurements_dto = ms.get_measurements()
            measurements = serializers.serialize('json', measurements_dto)
            return HttpResponse(measurements, 'application/json')

    if request.method == 'POST':
        measurement_dto = ms.create_measurement(json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')
    if request.method == 'DELETE':
        ms.delete_measurement(json.loads(request.body))
        return HttpResponse("Deleted", 'application/json')
        
@csrf_exempt
def measurement_view(request, pk):
    if request.method == 'GET':
        measurement_dto = ms.get_measurement(pk)
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')

    if request.method == 'PUT':
        measurement_dto = ms.update_measurement(pk, json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')
    if request.method == 'DELETE':      
        ms.delete_measurement(pk)
        return HttpResponse("Deleted", 'application/json')
    if request.method == 'PATCH':   
        measurement_dto = ms.patch_measurement(pk, json.loads(request.body))
        measurement = serializers.serialize('json', [measurement_dto,])
        return HttpResponse(measurement, 'application/json')