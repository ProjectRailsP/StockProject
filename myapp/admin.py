from django.contrib import admin

# Register your models here.
from myapp.models import FavoriteStocks, NotificationsRules, NotificationType, User
from myapp.models import Notifications
admin.site.register(FavoriteStocks)
admin.site.register(Notifications)
admin.site.register(NotificationsRules)
admin.site.register(NotificationType)
admin.site.register(User)
