from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.db import IntegrityError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewUserForm
from .models import Profile

# Create your views here.
# def register(request):
#     # now we need to handle the post request
#     if request.method == 'POST':
#         form = NewUserForm(request.POST)
#         if form.is_valid():
#             # pass
#             user = form.save()  #so when we call the form.save() it calls the function from form.py and it returns user so we need to catch the user and to do that we catch it through user =
#             return redirect('myapp/products')
#     form = NewUserForm()
#     context =  {
#         'form':form
#     }
#     return render(request, 'users/register.html', context)


# This may work

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password1')
            user = authenticate(request, username=username, password=password, email=email)
            if user is not None:
                login(request, user)
                return redirect('myapp/products')  # Replace 'home' with the desired redirect URL after successful registration
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'users/profile.html')

# def create_profile(request):
#     if request.method == 'POST':
#         contact_number = request.POST.get('number')
#         image = request.FILES['upload']
#         user = request.user
#         profile = Profile(user=user,image=image, contact_number=contact_number)
#         profile.save()
#     return render(request, 'users/createprofile.html')

def create_profile(request):
    if request.method == 'POST':
        contact_number = request.POST.get('number')
        image = request.FILES['upload']
        user = request.user

        # Check if a profile already exists for the user
        profile, created = Profile.objects.get_or_create(user=user)

        # Update the profile fields
        profile.image = image
        profile.contact_number = contact_number

        try:
            profile.save()
        except IntegrityError:
            # Handle the case where a unique constraint is violated
            # For example, display an error message or redirect to an appropriate page
            return HttpResponse("Error: Profile already exists")

    return render(request, 'users/createprofile.html')