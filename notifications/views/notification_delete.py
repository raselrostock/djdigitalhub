from django.shortcuts import render, redirect

# Model
from notifications.models import Notification

# Delete a specific notification
def DeleteNotificationView(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.delete()
    return redirect('notifications:notifications')
