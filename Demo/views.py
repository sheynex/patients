from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Function to render the Home Page
def frontend(request):
    return render(request, "frontend.html")

# Function to render the Backend Page
@login_required(login_url = "login")
def backend(request):
    return render(request, "backend.html")

