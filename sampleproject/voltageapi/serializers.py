from rest_framework import serializers
from voltageapi.models import measurement

class MeasurementSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = measurement
        fields = ('id', 'voltage', 'current', 'power','time_added','time_measured')
