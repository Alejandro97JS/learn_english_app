from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class CategoryLabel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    name_spanish = models.TextField(null = True, blank = True, default = None)
    description = models.TextField(null = True, blank = True, default = None)
    description_spanish = models.TextField(null = True, blank = True, default = None)

    def __str__(self):
        return self.name

class Label(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    name = models.TextField()
    name_spanish = models.TextField(null = True, blank = True, default = None)
    description = models.TextField(null = True, blank = True, default = None)
    description_spanish = models.TextField(null = True, blank = True, default = None)

    def __str__(self):
        return self.name

class Example(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.TextField()
    text_spanish = models.TextField(null = True, blank = True, default = None)

    def __str__(self):
        return self.text

class LanguageStyle(models.TextChoices):
    VERY_FORMAL = "VF", _("Very Formal")
    FORMAL = "F", _("Formal")
    INFORMAL = "I", _("Informal")
    VERY_INFORMAL = "VI", _("Very Informal")
    NOT_SPECIFIED = "NS", _("Not Specified")