from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.http import HttpResponse
from urllib import request
from .models import *
from .forms import *


# /----- Views for Homepage -----/
def home(request):


    

    context = {}
    return render(request, 'home.html', context)


# /----- Views for signup -----/
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']


        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username exist")
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.error(request, "This email is already used")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password1)
                user.save()
                auth.login(request, user)

                # messages.info(request, "User successfully created")
                return redirect('/')
        else:
            messages.error(request, "Password not matching")
            return redirect('register')
    else:
        return render(request, 'register.html')
    

# /----- Views for Signin -----/
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "Wrong username or password")
            return redirect('login')
            # return HttpResponseRedirect('/')
    else:
        return render(request, 'login.html')


# /----- Views for Logout -----/
def logout(request):
    auth.logout(request)
    return redirect('/')

# /----- Views for Occupants -----/
def occupant(request):
    occupant = occupants.objects.all()
    if request.method == 'POST':
        form = OccupantsForm(request.POST)
        if form.is_valid():
            occupant_name = request.POST['occupant_name']

            if occupants.objects.filter(occupant_name=occupant_name).exists():
                messages.error(request, "Occupant exist")
                return redirect('occupants')
            else:
                occupant = form.save(commit=False)
                occupant.save()

                return redirect('occupants')
    else:
        form = OccupantsForm()

    

    context = {'form': form, 'occupant': occupant}
    return render(request, 'occupants.html', context)


# /----- Views for Floors -----/
def floor(request):
    floor = floors.objects.all()
    if request.method == 'POST':
        form = FloorsForm(request.POST)
        if form.is_valid():
            floor_name = request.POST['floor_name']

            if floors.objects.filter(floor_name=floor_name).exists():
                messages.error(request, "Floor already exist")
                return redirect('floors')
            else:
                occupant = form.save(commit=False)
                occupant.save()

                return redirect('floors')
    else:
        form = FloorsForm()

    

    context = {'form': form, 'floor': floor}
    return render(request, 'floors.html', context)


# /----- Views for Floors Unit -----/
def unit(request):
    unit = locations.objects.all()
    if request.method == 'POST':
        form = UnitForm(request.POST)
        if form.is_valid():
            unit = form.save(commit=False)
            unit.save()

            return redirect('units')
    else:
        form = UnitForm()

    

    context = {'form': form, 'unit': unit}
    return render(request, 'units.html', context)
