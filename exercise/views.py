from django.shortcuts import render
from .models import exercises, detail

def details(request, exercise_id):
    exercise = exercises.objects.get(pk=exercise_id)
    exercise_details = detail.objects.filter(exercises=exercise)
    return render(request, 'details.html', {'exercise_details': exercise_details})

