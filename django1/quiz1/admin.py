from django.contrib import admin
from .models import CustomUser, Quiz, Question, Response

admin.site.register(CustomUser)
admin.site.register(Quiz)
admin.site.register(Question)
admin.site.register(Response)
