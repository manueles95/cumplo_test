from django.shortcuts import render
from series_values.models import SeriesIndex
from series_values.models import TiieIndex
from rest_framework.views import APIView
from rest_framework.response import Response
from series_values.serializers import SeriesInformationSerializer
from django.http import Http404
import requests
from rest_framework.renderers import TemplateHTMLRenderer
from requests.exceptions import HTTPError
from rest_framework import status

class ResponseObject:
  def __init__(self, series_id, series_name, average_value, min_value, max_value):
    self.series_id = series_id
    self.series_name = series_name
    self.average_value = average_value
    self.min_value = min_value
    self.max_value = max_value

class SeriesInformation(APIView):
    """
    Retrieve information from Banxico
    Calculate information corresponding to series
    """

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'sereies_values.html'

    def get_object(self, front_id):
        try:
            return SeriesIndex.objects.get(front_identifier=front_id)
        except SeriesIndex.DoesNotExist:
            raise Http404

    def calculateAverage(self, list):
        return round(sum(list) / len(list), 2)

    def getMinValue(self, list):
        return round(min(list), 2)

    def getMaxValue(self, list):
        return round(max(list), 2)

    def get(self, request, front_id, init_date, end_date, format=None):

        series_index = self.get_object(front_id)

        base_url = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series'
        final_url = '/'.join([base_url, series_index.series_id, 'datos', init_date, end_date])
        headers = {'Bmx-Token': 'c246391fa2f90dbd58deea3279c57ed72a46f659a0a082f48287c221f62ea2ac'}
        try:
            response = requests.get(final_url, headers=headers)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'GTTP errror occurred: {http_err}')
            return Response(status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            print(f'Other error occurres: {err}')
            return Response(status=500)

        series_response = response.json()
        values_arr = []
        dates_arr = []

        try:
            series_data = series_response['bmx']['series'][0]['datos']
            for dato in series_data:
                values_arr.append(float(dato['dato']))
                date = str(dato['fecha'])
                dates_arr.append(date)


            average_value = self.calculateAverage(values_arr)
            min_value = self.getMinValue(values_arr)
            max_value = self.getMaxValue(values_arr)

            response1 = ResponseObject(series_index.series_id, series_index.front_identifier, average_value, min_value, max_value)
            serializer = SeriesInformationSerializer(response1)
        except KeyError:
            response1 = ResponseObject(series_index.series_id, series_index.front_identifier, 0, 0, 0)
            serializer = SeriesInformationSerializer(response1)


        context = {
            'series_general_info': serializer.data,
            'series_chart_info': {
                'intial_date': init_date,
                'end_date': end_date,
                'series_values': values_arr,
                'series_dates': dates_arr
            }
        }
        return Response(context)



class TiieComparisson(APIView):
    """
    Retreive information from the different tiies
    Resturns comparisson of all the tiies, includes graphs
    """

    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'tiie_comparisson.html'

    def getMaxValue(self, list):
        return round(max(list), 2)

    def get(self, request, initial_date, end_date):


        base_url = 'https://www.banxico.org.mx/SieAPIRest/service/v1/series'
        headers = {'Bmx-Token': 'c246391fa2f90dbd58deea3279c57ed72a46f659a0a082f48287c221f62ea2ac'}

        tiies = TiieIndex.objects.all()
        tiies_arr = []

        for tiie_item in tiies:

            final_url = '/'.join([base_url, tiie_item.tiie_id, 'datos', initial_date, end_date])
            try:
                print('entering try to get request')
                response = requests.get(final_url, headers=headers)
                response.raise_for_status()
            except HTTPError as http_err:
                print(f'GTTP errror occurred: {http_err}')
                return Response(status=status.HTTP_400_BAD_REQUEST)
            except Exception as err:
                print(f'Other error occurres: {err}')
                return Response(status=500)

            tiie_response = response.json()
            values_arr = []
            dates_arr = []

            try:
                tiie_data = tiie_response['bmx']['series'][0]['datos']

                for dato in tiie_data:
                    values_arr.append(float(dato['dato']))
                    date = str(dato['fecha'])
                    dates_arr.append(date)

                max_value = self.getMaxValue(values_arr)
                tiie_object = {
                    'term': tiie_item.term,
                    'description': tiie_item.description,
                    'values': values_arr,
                    'dates': dates_arr,
                    'max_value': max_value
                }
            except KeyError:
                tiie_object = {
                    'term': tiie_item.term,
                    'description': tiie_item.description,
                    'values': values_arr,
                    'dates': dates_arr,
                    'max_value': 0
                }

            tiies_arr.append(tiie_object)

        context = {
            'data_for_graph': tiies_arr,
            'initial_date': initial_date,
            'end_date': end_date
        }

        return Response(context)


class Base(APIView):
    """
    Base api endpooint
    Shows empty body with nav var
    """
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'base.html'
    def get(self, request):
        return Response()
