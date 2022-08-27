from ..models import Measurement

def  get_measurements():
    measurements = Measurement.objects.all()
    return measurements

