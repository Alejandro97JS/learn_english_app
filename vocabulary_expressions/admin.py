from django.contrib import admin

from . import models as m

# Register your models here.

@admin.register(m.Entry)
class EntryAdmin(admin.ModelAdmin):
    list_display = ["title", "pronunciation_notes", "description"]
    list_filter = ["category_labels", "labels", "language_style"]
    search_fields = ["title", "spanish_title", "description", "spanish_description", "pronunciation_notes"]
    date_hierarchy = "created_at"
    readonly_fields = ["created_at"]