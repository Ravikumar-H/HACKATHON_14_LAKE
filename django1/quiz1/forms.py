from django import forms
from .models import Quiz, Question, Response

class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'assigned_class', 'deadline', 'time_limit']

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text', 'question_type', 'options', 'correct_answer']

class ResponseForm(forms.ModelForm):
    class Meta:
        model = Response
        fields = ['answer']
