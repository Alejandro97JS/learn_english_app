from django.contrib import admin
from . import models as m

# Register your models here.

@admin.register(m.CategoryLabel)
class CategoryLabelAdmin(admin.ModelAdmin):
    list_display = ["name", "name_spanish", "description", "description_spanish"]
    search_fields = ["name", "name_spanish", "description", "description_spanish"]
    date_hierarchy = "created_at"
    readonly_fields = ["created_at"]

@admin.register(m.Label)
class LabelAdmin(admin.ModelAdmin):
    list_display = ["name", "name_spanish", "description", "description_spanish"]
    search_fields = ["name", "name_spanish", "description", "description_spanish"]
    date_hierarchy = "created_at"
    readonly_fields = ["created_at"]