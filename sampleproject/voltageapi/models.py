from django.db import models

class measurement(models.Model):
    voltage= models.FloatField()
    current = models.FloatField()
    power =models.FloatField()
    total_power = models.FloatField()
    time_added = models.DateTimeField(auto_now_add=True)
    time_measured = models.DateTimeField()
    def __str__(self):
        return str(self.time_measured)

class zone(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    def __sr__(self):
        return str(self.start_time)+" to "+str(self.end_time)
class temp(models.Model):
    current_zone_value = models.FloatField()
    last_zone_value = models.FloatField()
    current_zone = models.ForeignKey('zone', models.DO_NOTHING,related_name="cur_zone")
    last_zone = models.ForeignKey('zone', models.DO_NOTHING,related_name="lst_zone")
    current_monthly_accumulate = models.ForeignKey('monthly_accumulate', models.DO_NOTHING)
    def __str__(self):
        return str(self.current_zone_value)
class monthly_accumulate(models.Model):
    zone1 = models.FloatField(blank=True, null=True)
    zone2 = models.FloatField(blank=True, null=True)
    zone3 = models.FloatField(blank=True, null=True)
    zone4 = models.FloatField(blank=True, null=True)
    month = models.IntegerField(blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)  # This field type is a guess.
