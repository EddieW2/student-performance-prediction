import joblib
import pandas as pd

from django.shortcuts import render, redirect, get_object_or_404

from .forms import StudentPredictionForm
from .models import StudentPrediction

model = joblib.load("ml_model/student_performance_model.pkl")

def student_input(request):
    if request.method == 'POST':
        form = StudentPredictionForm(request.POST)

        if form.is_valid():
            student = form.save(commit=False)
            absences = round((100 - student.attendance) / 5)
            student_data = pd.DataFrame([{
                'age': student.age,
                'studytime': student.study_time,
                'absences': absences,
                'G1': student.previous_grade / 5,
                'G2': student.assignment_score / 5,
            }])
            prediction = model.predict(student_data)[0]
            
            probabilities = model.predict_proba(student_data)[0]

            predicted_index = list(model.classes_).index(prediction)

            probability = probabilities[predicted_index] * 100

            student.prediction = prediction
            student.prediction_probability = probability
            student.save()

            return redirect(
                'prediction_result',
                student_id=student.id
            )

    else:
        form = StudentPredictionForm()

    return render(request, 'predictor/student_input.html', {
        'form': form
    })


def prediction_result(request, student_id):
    student = get_object_or_404(
        StudentPrediction,
        id=student_id
    )

    return render(
        request,
        'predictor/prediction_result.html',
        {
            'student': student
        }
    )