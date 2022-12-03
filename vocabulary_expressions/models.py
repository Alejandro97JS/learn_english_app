from django.db import models

from generic.models import CategoryLabel, Label, LanguageStyle

# Create your models here.
class Entry(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.TextField()
    spanish_title = models.TextField(null = True, blank = True, default = None)
    description = models.TextField(null = True, blank = True, default = None)
    spanish_description = models.TextField(null = True, blank = True, default = None)
    pronunciation_notes = models.TextField(null = True, blank = True, default = None)
    category_labels = models.ManyToManyField(CategoryLabel)
    labels = models.ManyToManyField(Label)
    language_style = models.CharField(max_length=2, choices=LanguageStyle.choices,
        default=LanguageStyle.NOT_SPECIFIED)