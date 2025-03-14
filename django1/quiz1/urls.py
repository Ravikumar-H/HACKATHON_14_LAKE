from django.urls import path
from . import views

urlpatterns = [
    path('create_quiz/', views.create_quiz, name='create_quiz'),
    path('view_quizzes/', views.view_quizzes, name='view_quizzes'),
    path('attempt_quiz/<int:quiz_id>/', views.attempt_quiz, name='attempt_quiz'),
]
