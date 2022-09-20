from zoneinfo import available_timezones
from django.contrib import admin
from app.models import Facility, State,City,Hospital,Availability

from django.db.models.signals import post_save
from django.dispatch import receiver

# Register your models here.
@receiver(post_save, sender=Hospital)
def aferHospitalSave(signal,instance,**kwargs):
   facilities = Facility.objects.all()
   for facility in facilities:
       availability = Availability(hospital= instance, facility = facility)
       availability.save()
    


@receiver(post_save, sender=Facility)
def aferFacilitySave(signal,instance,**kwargs):
   hospitals = Hospital.objects.all()
   for hospital in hospitals:
       availability = Availability(hospital= hospital, facility = instance)
       availability.save()










    

class FacilityAdmin(admin.ModelAdmin):
    model: Facility
    list_display=['title']

class HospitalAdmin(admin.ModelAdmin):
    model: Hospital
    list_display=['name','phone','address','city']

class AvailabilityAdmin(admin.ModelAdmin):
    model: Availability
    list_display=['hospital','facility','total','available']
    list_editable = ['total' , 'available']





admin.site.register(State)
admin.site.register(City)

admin.site.register(Hospital,HospitalAdmin)

admin.site.register(Facility,FacilityAdmin)
admin.site.register(Availability,AvailabilityAdmin)



