from django.shortcuts import render

from measurements.models import Measurement

from .logic import measurements_logic as ms
from measurements.logic.measurements_logic import get_measurements
from django.http import HttpResponse
from django.core import serializers
import json
def measurements_view(request):
    if request.method == "GET":
        measurements = ms.get_measurements()
        measurements_dto= serializers.serialize('json', measurements_dto)
        return render(request, "measurements.html", {"measurements": measurements})
    