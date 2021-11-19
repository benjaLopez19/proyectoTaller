from django.contrib import admin

from dashboard.models import Data

# Register your models here.

class DataAdmin(admin.ModelAdmin):
    list_display=("id","intent", "evaluacion", "clasificacion", "sub_clasificacion","conversation_id","confidence")
    search_fields=("id","intent", "evaluacion", "clasificacion", "sub_clasificacion","conversation_id","mensaje_usuario","respuesta_bot","fecha")
    list_filter=("clasificacion","fecha","evaluacion") #"intent", "evaluacion", 


admin.site.register(Data, DataAdmin)