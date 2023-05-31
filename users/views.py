from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import NewUserForm

# Create your views here.
def register(request):
    # now we need to handle the post request
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            # pass
            user = form.save()  #so when we call the form.save() it calls the function from form.py and it returns user so we need to catch the user and to do that we catch it through user =
            return redirect('myapp/products')
    form = NewUserForm()
    context =  {
        'form':form
    }
    return render(request, 'users/register.html', context)

@login_required
def profile(request):
    return render(request, 'users/profile.html')