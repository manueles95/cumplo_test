from django.urls import path, include
from series_values import views

urlpatterns = [
    path('series/<front_id>/<init_date>/<end_date>', views.SeriesInformation.as_view())
]
