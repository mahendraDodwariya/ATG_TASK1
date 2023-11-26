 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import UserForm, UserProfileForm


def signup(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST, request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            user_type_is = profile.user_type
            login(request, user)
            print(user_type_is)
            return redirect('dashboard', user_type=user_type_is)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'signup.html', {'user_form': user_form, 'profile_form': profile_form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            user_type = user.userprofile.user_type
            return redirect('dashboard', user_type=user_type)   
        else:
            messages.error(request, 'Invalid login credentials. Please try again or sign up.')
            return redirect('signup')
    return render(request, 'login.html')

 
def dashboard(request, user_type):
    if request.user.is_authenticated:
        template_name = f'{user_type}_dashboard.html'
        return render(request, template_name, {'user': request.user})
    else:
        
        return redirect('login')