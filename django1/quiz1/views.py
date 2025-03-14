from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Quiz, Question, Response
from .forms import QuizForm, QuestionForm, ResponseForm
from django.utils import timezone
from django.shortcuts import redirect

def home(request):
    return redirect('view_quizzes')  # Redirect students to their assigned quizzes
from django.shortcuts import render

def home(request):
    return render(request, 'quiz1/home.html')

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Quiz  # Assuming you have a Quiz model

@login_required
def view_quizzes(request):
    quizzes = Quiz.objects.filter(assigned_class=request.user.class_assigned)
    return render(request, 'quiz1/view_quizzes.html', {'quizzes': quizzes})

# Create Quiz
@login_required
def create_quiz(request):
    if request.user.role != 'teacher':
        return redirect('home')
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.teacher = request.user
            quiz.save()
            return redirect('quiz_list')
    else:
        form = QuizForm()
    return render(request, 'quiz1/create_quiz.html', {'form': form})

# View Assigned Quizzes (Student)
@login_required
def view_quizzes(request):
    quizzes = Quiz.objects.filter(assigned_class=request.user.class_assigned, deadline__gt=timezone.now())
    return render(request, 'quiz1/view_quizzes.html', {'quizzes': quizzes})

# Attempt Quiz
@login_required
def attempt_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()

    if request.method == 'POST':
        for question in questions:
            answer = request.POST.get(f'answer_{question.id}')
            Response.objects.create(
                quiz=quiz, student=request.user, question=question, answer=answer
            )
        return redirect('quiz_list')

    return render(request, 'quiz1/attempt_quiz.html', {'quiz': quiz, 'questions': questions})
