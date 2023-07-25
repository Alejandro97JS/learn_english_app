from django.urls import path

from . import views

app_name = "pdf_generator"

urlpatterns = [
    path("vocabulary_expressions", views.generate_vocabulary_pdf,
        name="vocabulary_expressions")
]
