from django.urls import path
from . import views


urlpatterns = [
    path('', views.student_input, name='student_input'),
    path(
        'result/<int:student_id>/',
        views.prediction_result,
        name='prediction_result'
    ),
]