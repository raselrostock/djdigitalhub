from django.db import models


class Membership(models.Model):
    MEMBERSHIP_TYPES = (
        ('Free', 'free'),
        ('Professional', 'pro'),
        ('Enterprise', 'ent')
    )
    slug = models.SlugField(max_length=64)
    membership_type = models.CharField(
        choices=MEMBERSHIP_TYPES, max_length=32, default='Free')
    stripe_plan_id = models.CharField(max_length=64)
    price = models.DecimalField(max_digits=5, decimal_places=2, default=0.0)

    class Meta:
        verbose_name = 'Membership'
        verbose_name_plural = 'Memberships'

    def __str__(self):
        return self.membership_type
