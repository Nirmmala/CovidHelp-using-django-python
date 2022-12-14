from django.shortcuts import render
from django.http import HttpResponse
from app.models import Availability, Facility, Hospital, State, City
from django.views import generic
# Create your views here.

class HospitalDetailsView(generic.DetailView):
    model = Hospital



def home(request):

    selected_state_id = request.GET.get('state')
    selected_city_id = request.GET.get('city')
    selected_facility_id = request.GET.get('facility')

    facilities = Facility.objects.all().order_by('pk')

    if selected_state_id:
        cities = City.objects.filter(state=selected_state_id)
    else:
        cities = City.objects.all()

    states = State.objects.all()
    
    if selected_city_id:
        hospitals = Hospital.objects.filter(city = selected_city_id)
    else:
        hospitals = Hospital.objects.all()

    if selected_facility_id:
        availabilities = Availability.objects.all()
        if selected_city_id:
            availabilities = availabilities.filter(hospital__city = City(pk = selected_city_id))
            
        availabilities = availabilities.filter(facility = Facility(pk =selected_facility_id), 
        available__gt=0)
        hospitals = []
        for avl in availabilities:
            hospitals.append(avl.hospital)
        print("hospital", hospitals)

    context = {
        'facilities':facilities,
        'cities' : cities,
        'states' :states,
        'hospitals' : hospitals,
        'selected_state_id' :selected_state_id,
        'selected_city_id' :selected_city_id,
        'selected_facility_id' :selected_facility_id,
        
    }
   
    return render(request, 'app/index.html',context=context)