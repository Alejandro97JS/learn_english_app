from django.urls import path

from . import views

app_name = "generic"

urlpatterns = [
    path("overall_statistics", views.recalculate_overall_statistics,
        name="recalculate_overall_statistics")
]
