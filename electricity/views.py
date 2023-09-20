from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import *


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
def occupants(request):
    # occupant = occupants.objects.all()


    

    # context = {'occupant': occupant,}
    return render(request, 'occupants.html')
