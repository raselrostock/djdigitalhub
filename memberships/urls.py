from django.urls import path
from memberships.views import (
    DashboardView,
    MembershipListView,
    PaymentView,
    updateTransactionRecords,
    CancelSubscription
)

app_name = 'memberships'

urlpatterns = [
    path('', DashboardView, name='dashboard')
]
