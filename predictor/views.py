from django.shortcuts import render, redirect
from .forms import StudentPredictionForm


def student_input(request):
    if request.method == 'POST':
        form = StudentPredictionForm(request.POST)

        if form.is_valid():
            student = form.save()
            return redirect('prediction_result', student_id=student.id)

    else:
        form = StudentPredictionForm()

    return render(request, 'predictor/student_input.html', {
        'form': form
    })


def prediction_result(request, student_id):
    return render(request, 'predictor/prediction_result.html')