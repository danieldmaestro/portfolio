from django.shortcuts import render
from .models import Project, Dev, Skill, Stack
from .forms import VisitorForm

# Create your views here.
# Define the views for the website

def home(request):
    projects = Project.objects.all()
    dev = Dev.objects.get()
    skills = Skill.objects.all()
    stack = Stack.objects.all()

    if request.method == 'POST':
        form = VisitorForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = VisitorForm()

    context = {
        'projects': projects,
        'dev': dev,
        'skills': skills,
        'stack': stack,
        'form': form,
    }


    return render(request, 'myapp/home.html', context)


