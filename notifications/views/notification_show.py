from django.shortcuts import render, redirect

# Model
from notifications.models import Notification

# Show a specific notification
def ShowNotificationView(request, notification_id):
    notification = Notification.objects.get(id=notification_id)
    notification.viewed = True
    notification.save()
    return render(request, 'notifications/notifications_show.html', {'notification': notification})
