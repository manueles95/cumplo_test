from rest_framework import serializers


class SeriesInformationSerializer(serializers.Serializer):


    series_id = serializers.CharField(read_only=True)
    series_name = serializers.CharField()
    average_value = serializers.FloatField()
    min_value = serializers.FloatField()
    max_value = serializers.FloatField()
