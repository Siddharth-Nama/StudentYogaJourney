from django.db import models

# Create your models here.
class exercises(models.Model):
    choicesin = (
    ('basicyogaroutine' , 'basicyogaroutine'),
    ('intermediateyogaroutine', 'intermediateyogaroutine'),
    ('advancedyogaroutine','advancedyogaroutine'),
    ('basicyoga','basicyoga'),
    ('intermediateyoga','intermediateyoga'),
    ('advancedyoga','advancedyoga'),
    ('basicmeditation','basicmeditation'),
    ('intermediatemeditation','intermediatemeditation'),
    ('advancedmeditation','advancedmeditation'),
    ('basicrelaxation','basicrelaxation'),
    ('intermediaterelaxation','intermediaterelaxation'),
    ('advancedrelaxation','advancedrelaxation')
    )
    exercisename = models.CharField(max_length=100)
    exerciseimage = models.ImageField(upload_to='exerciseimage')
    exercisetype = models.CharField(max_length=100 , choices=choicesin)

    def __str__(self):
        return self.exercisetype + " -> " + self.exercisename

class detail(models.Model):
    exercises = models.ForeignKey(exercises, on_delete=models.CASCADE)
    exerciseexplanation = models.TextField(max_length=10000)
    exercisesteps = models.TextField(max_length=10000)
    exercisevideo = models.URLField(max_length=500)
     
    def __str__(self):
        return self.exercises.exercisetype + " -> " + self.exercises.exercisename
 