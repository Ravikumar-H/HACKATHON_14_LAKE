from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = [
        ('teacher', 'Teacher'),
        ('student', 'Student'),
        ('admin', 'Admin'),
    ]
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    class_assigned = models.CharField(max_length=50, blank=True, null=True)

    # Add related_name to avoid conflicts
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_permissions_set',
        blank=True
    )


# Quiz Model
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    teacher = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='created_quizzes')
    assigned_class = models.CharField(max_length=50)
    deadline = models.DateTimeField()
    time_limit = models.PositiveIntegerField(help_text="Time limit in minutes")

# Question Model
class Question(models.Model):
    QUESTION_TYPES = [
        ('mcq', 'Multiple Choice Question'),
        ('short', 'Short Answer'),
        ('true_false', 'True/False'),
    ]
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    question_type = models.CharField(max_length=10, choices=QUESTION_TYPES)
    options = models.JSONField(blank=True, null=True)  # For MCQs
    correct_answer = models.CharField(max_length=200, blank=True, null=True)

# Response Model
class Response(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name='responses')
    student = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    score = models.FloatField(default=0)
