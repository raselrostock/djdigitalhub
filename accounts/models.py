from decouple import config
from datetime import datetime

# Django Module
from django.db import models
from django.conf import settings

# Thirdparty Module
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill

# Model
from django.contrib.auth.models import User
from memberships.models import Membership
from courses.models import Course

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY


class Profile(models.Model):
    user                    = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True)
    membership              = models.ForeignKey(
        'memberships.Membership', on_delete=models.SET_NULL, null=True)
    stripe_customer_id      = models.CharField(max_length=128)
    profile_pic             = ProcessedImageField(default='avatar.jpg', upload_to='profile-img/', processors=[
                                      ResizeToFill(200, 200)], format='JPEG', options={'quality': 60})

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'


class Subscription(models.Model):
    profile                 = models.ForeignKey(
        Profile, on_delete=models.CASCADE)
    stripe_subscription_id  = models.CharField(max_length=64)
    active                  = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Subscription'
        verbose_name_plural = 'Subscriptions'

    def __str__(self):
        return self.profile.user.username

    @property
    def get_next_billing_date(self):
        subscription = stripe.Subscription.retrieve(
            self.stripe_subscription_id)
        return datetime.fromtimestamp(subscription.current_period_end)
