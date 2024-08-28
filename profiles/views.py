from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from profiles.models import Projects


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
    
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname

        myuser.save()

        messages.success(request, "Your Account has been successfully created.")

        return redirect('signup')  # Assuming 'signin' is the name of the URL pattern for your sign-in view
    
    return render(request, 'signup.html')

    
    
    
    return render(request, 'signup.html', {'user': request.user})

def signin(request):   

    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']

        user = authenticate(username=username, password=pass1)

        if user is not None:
            login(request, user)
            if not user.is_superuser:
                messages.error(request, "Bad credential")
                fname = user.first_name
                return HttpResponseRedirect(reverse("home"))
            else:
                messages.error(request, "Bad credentials")
                return redirect('signin')
        
        else:
            messages.error(request, "Bad Credential")
            return redirect('signin')

    return render(request, 'signin.html')


def home(request):

    profile = request.user
    projects = Projects.objects.filter(user=request.user)
    context = {
        'user' : profile,
        'projects': projects,
    }
    return render(request, 'home.html',context)

def add_work(request):
    if request.method == 'POST':
        username = request.POST['username']
        project_name = request.POST['project_name']
        link = request.POST['link']
        print(username, project_name, link)

        # Create a new project instance instead of fetching and updating the existing one
        rec = Projects(user=request.user, project_name=project_name, link=link)
        rec.save()

        return HttpResponseRedirect(reverse("home"))

    profile = request.user
    context = {
        'user': request.user,
    }
    return render(request, 'add_work.html', context)

