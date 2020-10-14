import datetime

# Django Module
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404

# Decorator
from django.contrib.auth.decorators import login_required

# Model
from courses.models import Review, Course

# Form
from courses.forms import ReviewForm

@login_required
def AddReviewView(request, course_slug):
    course = get_object_or_404(Course, slug=course_slug)
    form = ReviewForm(request.POST)
    review_qr = Review.objects.filter(user=request.user, course=course)
    if review_qr.exists():
        messages.warning(request, 'You already reviewed on this course')
        return redirect('courses:course-detail', course_slug)
    else:
        if form.is_valid():
            rating = form.cleaned_data['rating']
            comment = form.cleaned_data['comment']
            review = Review()
            review.course = course
            review.pub_date = datetime.datetime.now()
            review.user = request.user
            review.comment = comment
            review.rating = rating
            review.save()
            messages.success(request, 'Successfully reviewed')
            return redirect('courses:course-detail', course_slug)
        return render(request, 'courses/course_detail.html', {'form': form, 'course': course})