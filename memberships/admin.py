from django.contrib import admin

# Model
from memberships.models import Membership


class MembershipAdmin(admin.ModelAdmin):
    list_display = ['slug', 'membership_type', 'stripe_plan_id', 'price']
    list_filter = ['stripe_plan_id']


admin.site.register(Membership, MembershipAdmin)
