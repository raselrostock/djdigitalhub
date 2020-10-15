from datetime import date 
from django.conf import settings
from django.db import models
from django.db.models import Avg, Func
from django.db.models.signals import pre_save
from django.urls import reverse

# Third Party Module
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Utility Module
from djdigitalhub.utils import unique_slug_generator

# Model
from django.contrib.auth.models import User
from memberships.models import Membership
from instructors.models import Instructor

class Round(Func):
    function = 'ROUND'

class Course(models.Model):
    slug                    = models.SlugField('Slug', max_length=128, blank=True, unique=True)
    title                   = models.CharField('Title', max_length=128, blank=True, null=True)
    description             = RichTextUploadingField(blank=True, null=True)
    extra_info              = models.TextField('Extra Information', blank=True)
    thumbnail               = ProcessedImageField(default='course_bg.jpg', upload_to='course_img/',
                                    processors=[ResizeToFill(600, 350)],
                                    format='JPEG',
                                    options={'quality': 60})
    start_date              = models.DateField(
        verbose_name='Start Date', default=date.today, blank=True, null=True)
    likes                   = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)
    allowed_membership      = models.ManyToManyField(Membership)
    instructors             = models.ManyToManyField(Instructor)

    class Meta:
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse("courses:course-detail", kwargs={"course_slug": self.slug})

    def get_total_like(self):
        return self.likes.count()

    @property
    def reviews(self):
        return self.review_set.all().order_by('-pub_date')[:3]

    @property
    def review_average(self):
        return self.review_set.aggregate(rev_avg=Round(Avg('rating')))

def course_slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(
            instance, instance.title, instance.slug)


pre_save.connect(course_slug_save, sender=Course)


class Lesson(models.Model):
    slug                    = models.SlugField('Slug', max_length=128, blank=True, unique=True)
    title                   = models.CharField('Title', max_length=128, blank=True)
    description             = models.TextField('Description', blank=True)
    extra_info              = models.TextField('Extra Information', blank=True)
    thumbnail               = ProcessedImageField(default='lesson_bg.jpg', upload_to='lesson_img/',
                                    processors=[ResizeToFill(600, 350)],
                                    format='JPEG',
                                    options={'quality': 60})
    file_1                  = models.FileField(upload_to='lesson_doc/', null=True, blank=True)
    file_2                  = models.FileField(upload_to='lesson_doc/', null=True, blank=True)
    file_3                  = models.FileField(upload_to='lesson_doc/', null=True, blank=True)
    file_4                  = models.FileField(upload_to='lesson_doc/', null=True, blank=True)
    file_5                  = models.FileField(upload_to='lesson_doc/', null=True, blank=True)
    course                  = models.ForeignKey(
        Course, related_name='lessons', on_delete=models.SET_NULL, null=True)
    video_link              = models.CharField(
        'Video Link', max_length=300, blank=True, null=True)

    class Meta:
        verbose_name = 'Lesson'
        verbose_name_plural = 'Lessons'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("courses:lesson-detail", kwargs={
            "course_slug": self.course.slug,
            "lesson_slug": self.slug
        })

    @property
    def comments(self):
        return self.comment_set.all().order_by('-comment_at').order_by('author').filter(approved_comment=True)[:5]


def lesson_slug_save(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(
            instance, instance.title, instance.slug)


pre_save.connect(lesson_slug_save, sender=Lesson)

class Comment(models.Model):
    lesson                  = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    comment_at              = models.DateTimeField(
        verbose_name='Commented At', auto_now=True)
    author                  = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    msg                     = models.TextField('Message', blank=True)
    approved_comment        = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        ordering = ['-comment_at', 'author']

    def __str__(self):
        return self.msg

    def approve(self):
        self.approved_comment = True
        self.save()


class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5')
    )
    course                  = models.ForeignKey(Course, on_delete=models.CASCADE)
    pub_date                = models.DateTimeField(
        verbose_name='Published Date', auto_now=True)
    user                    = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE)
    comment                 = models.TextField(blank=True)
    rating                  = models.IntegerField(choices=RATING_CHOICES)

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'

    def __str__(self):
        return self.comment