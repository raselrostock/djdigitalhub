import datetime

# Django Module
from django.utils import timezone
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

# Decorator
from quizes.decorators import restrict_quiz

# Model
from notifications.models import Notification
from quizes.models import Quiz, Question, QuizParticipation
from courses.models import Course, Lesson


@login_required
@restrict_quiz("Enterprise")
def QuizView(request, course_slug, lesson_slug):
    course = Course.objects.get(slug=course_slug)
    lesson = Lesson.objects.get(slug=lesson_slug)
    quiz = Quiz.objects.get(lesson__slug=lesson.slug)
    questions = Question.objects.filter(quiz__title=quiz.title).all()
    context = {
        'questions': questions,
        'course_slug': course_slug,
        'lesson_slug': lesson_slug
    }
    return render(request, 'quizes/quiz.html', context)