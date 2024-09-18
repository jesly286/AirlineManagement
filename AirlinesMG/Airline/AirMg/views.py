from django.shortcuts import render, redirect

from .forms import LoginForm, FlightForm
from .models import Flight


# Create your views here.
def login_view(request):

    predefined_username = 'Jesly'
    predefined_password = 'jess@123'

    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            if username == predefined_username and password == predefined_password:
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'form': form, 'error': 'Invalid username or password'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})



def dashboard(request):
    return render(request, 'dashboard.html')



def flight_list(request):
    flights = Flight.objects.all()
    return render(request, 'flight_list.html', {'AirMg': flights})


def flight_search(request):
    if request.method == 'POST':
        dep_airport = request.POST['dep_airport']
        arr_airport = request.POST['arr_airport']

        flights = Flight.objects.filter(DepAirport=dep_airport, ArrAirport=arr_airport)

        if flights.exists():
            return render(request, 'flight_search.html', {'AirMg': flights})
        else:
            message = f"No flights found from {dep_airport} to {arr_airport}."
            return render(request, 'flight_search.html', {'message': message})
    else:
        return render(request, 'flight_search.html')


def flight_add(request):
    if request.method == 'POST':
        form = FlightForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm()
    return render(request, 'flight_add.html', {'form':form})


def flight_edit(request, flight_id):
    flight = Flight.objects.get(FlightId=flight_id)
    if request.method == 'POST':
        form = FlightForm(request.POST, instance=flight)
        if form.is_valid():
            form.save()
            return redirect('flight_list')
    else:
        form = FlightForm(instance=flight)
    return render(request, 'flight_edit.html', {'form': form})

def home(request):
    return render(request, 'home.html')
