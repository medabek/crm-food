from django.contrib import admin
from meal.models import MealCategory, Department, ServicePercentage, Status, Table
#from .serializers import CategorySerializers
# Register your models here.
admin.site.register(MealCategory)
admin.site.register(Department)
admin.site.register(ServicePercentage)
admin.site.register(Status)
admin.site.register(Table)
