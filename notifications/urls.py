from django.urls import path
from notifications.views.notification_list import NotificationListView
from notifications.views.notification_show import ShowNotificationView
from notifications.views.notification_delete import DeleteNotificationView

app_name = 'notifications'

urlpatterns = [
    path('', NotificationListView, name='notifications'),
    path('show/<notification_id>/', ShowNotificationView, name='show_notification'),
    path('delete/<notification_id>/',
         DeleteNotificationView, name='delete_notification'),
]
