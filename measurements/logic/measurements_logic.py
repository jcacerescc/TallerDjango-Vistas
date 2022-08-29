import datetime
from variables.models import Variable
from measurements.models import Measurement
from ..models import Measurement
from ..models import Variable

def  get_measurements():
    measurements = Measurement.objects.all()
    return measurements
def get_measurement(measurement_pk):
    measurement = Measurement.objects.get(pk=measurement_pk)
    return measurement
def create_measurement(new_measurement):
    measurement = Measurement(
        variable= Variable.objects.get(pk=new_measurement["variable"]["pk"]),
        value= new_measurement["value"],unit=new_measurement["unit"],
        place= new_measurement["place"],
        dateTime= datetime.datetime.now(),
    )
    measurement.save()
    return measurement

def update_measurement(measurement_pk, new_measurement):
    measurement = get_measurement(measurement_pk)
    measurement.value = new_measurement["value"]
    measurement.save()
    return measurement

def delete_measurement(measurement_pk): 
    measurement = Measurement.objects.get(pk=measurement_pk)
    measurement.delete()

def patch_measurement(measurement_pk, new_measurement):
    measurement = get_measurement(measurement_pk)
    measurement.value = new_measurement["value"]
    measurement.save()
    return measurement