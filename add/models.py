from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

class Location(models.Model):
    name = models.CharField(max_length=255)
    max_visitors = models.PositiveIntegerField()
    
    def __str__(self):
        return self.name
class Ad(models.Model):
    name = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()
    locations = models.ManyToManyField(Location)
    
    

    def __str__(self):
        return self.name
    
class DailyVisitor(models.Model):
    date = models.DateField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    ad = models.ForeignKey(Ad, on_delete=models.CASCADE)
    visitor_count = models.PositiveIntegerField(default=0)
    is_blocked=models.BooleanField(default=False)
    


    def __str__(self):
        return f"{self.date} - {self.location.name}: {self.visitor_count}"
    


    # def save(self, *args, **kwargs):
    # # Check if the daily visitor count exceeds the maximum allowed visitors for the location
    #  if self.visitor_count > self.location.max_visitors:
    #     # Set the is_blocked field of the current DailyVisitor instance to True
    #     raise ValidationError(f"Visitor count for this location has set ({self.location.max_visitors})")
    #  elif self.visitor_count>=self.location.max_visitors:
    #     # If the count is not exceeded, set the is_blocked field to False
    #     self.is_blocked = True
    #  else:
    # #    self.is_blocked = False
    # # Save the current DailyVisitor instance
    #  super(DailyVisitor, self).save(*args, **kwargs)

    class Meta:
        unique_together = ['location', 'ad']


