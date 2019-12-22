from django.urls import path, include
from series_values import views

urlpatterns = [
    path('', views.Base.as_view()),
    path('series/<front_id>/<init_date>/<end_date>', views.SeriesInformation.as_view(), name='series_information')
]
