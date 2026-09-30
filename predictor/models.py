from django.db import models

class StudentPrediction(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    attendance = models.FloatField()
    study_time = models.FloatField()
    previous_grade = models.FloatField()
    assignment_score = models.FloatField()
    participation = models.FloatField()

    prediction = models.CharField(max_length=20, blank=True)
    prediction_probability = models.FloatField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
