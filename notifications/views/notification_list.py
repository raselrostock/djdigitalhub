from django.shortcuts import render, redirect

# Model
from notifications.models import Notification


# Show the list of all notifications
def NotificationListView(request):
    notifications = Notification.objects.filter(
        user=request.user).all().order_by('-notification_at')
    return render(request, 'notifications/notifications_list.html', {'notifications': notifications})
