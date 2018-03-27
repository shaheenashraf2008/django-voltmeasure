from django.contrib import admin
from voltageapi.models import measurement,monthly_accumulate,zone,temp
from voltageview.models import UserProfileInfo
# Register your models here.
admin.site.register(measurement)
admin.site.register(monthly_accumulate)
admin.site.register(zone)
admin.site.register(temp)
admin.site.register(UserProfileInfo)
