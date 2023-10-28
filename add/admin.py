from django.contrib import admin
from .models import Ad,Location,DailyVisitor
from django.contrib import admin
from django.core.exceptions import ValidationError
from django.contrib import messages
# Register your models here.
@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'start_date', 'end_date')
    list_filter = ('start_date', 'end_date', 'locations')
    search_fields = ('name', 'locations__name')
    filter_horizontal = ('locations',)

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'max_visitors')

@admin.register(DailyVisitor)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('id','date', 'location','ad','visitor_count',)
  




    