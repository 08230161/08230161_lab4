from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import AboutMe, LearningJourney

@login_required
def index(request):
    journeys = LearningJourney.objects.all()
    return render(request, 'index.html', {'journeys': journeys})

@login_required
def about_me(request):
    about = AboutMe.objects.first()
    return render(request, 'aboutMe.html', {'about': about})
