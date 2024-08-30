from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import CustomUser
from exercise.models import exercises
@login_required(login_url="/login/")
def home(request):
    custom_user = request.user.customuser
    exercises_list = exercises.objects.all()
    return render(request, 'home.html',{'custom_user': custom_user, 'exercises_list': exercises_list})

def profile_view(request):
    custom_user = request.user.customuser 
    return render(request, 'profile.html', {'custom_user': custom_user})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid username or password")
            return redirect('/login/')
    
    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username already taken")
            return redirect('/register/')

        user = User.objects.create_user(username=username, password=password)
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        
        custom_user = CustomUser.objects.create(
            user=user,
            email='example2003@gmail.com',  
            phone='+91987654321',  
            dob='2003-04-26',  
            image=None  
        )
        
        messages.info(request, "Account created successfully")
        return redirect('/login/')
    
    return render(request, 'register.html')


def rename(request):
    if request.method == 'POST':
        image = request.FILES.get('image')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        dob = request.POST.get('dob')

        user = request.user
        custom_user = user.customuser  
        custom_user.email = email
        custom_user.phone = phone
        custom_user.dob = dob
        custom_user.image = image
        custom_user.save()

        messages.info(request, "Account Updated successfully")
        return redirect('/profile/')  # Redirect to the profile page
    
    return render(request, 'rename.html')

def exercise_search(request):
    query = request.GET.get('query', '')
    exercises_list = exercises.objects.all()
    results = []
    if query:
        results = exercises.objects.filter(exercisename__icontains=query)
        exercises_list = exercises.objects.all()

    return render(request, 'home.html', {'results': results, 'query': query , 'exercises_list':exercises_list})
