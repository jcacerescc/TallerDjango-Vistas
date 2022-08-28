from variables.models import Variable
from ..models import Measurement
from ..models import Variable

def  get_measurements():
    measurements = Measurement.objects.all()
    return measurements
def get_measurement(measurement_pk):
    measurement = Measurement.objects.get(pk=measurement_pk)
    return measurement
def create_measurement(var):
    measurement = Measurement(variable=var["variable"], value=var["value"], unit=var["unit"], place=var["place"], dateTime=var["dateTime"])
    measurement.save()
    return measurement

def update_measurement(measurement_pk, new_measurement):
    measurement = get_measurement(measurement_pk)
    measurement.value = new_measurement["value"]
    measurement.save()
    return measurement

def delete_measurement(measurement_pk): 
    measurement = get_measurement(measurement_pk)
    measurement.delete()

def patch_measurement(measurement_pk, new_measurement):
    measurement = get_measurement(measurement_pk)
    measurement.value = new_measurement["value"]
    measurement.save()
    return measurement