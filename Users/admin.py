from django.contrib import admin
from simple_history.admin import SimpleHistoryAdmin
from .models import User
# Register your models here.
class PollHistoryAdmin(SimpleHistoryAdmin):
    history_list_display = ["status"]
    search_fields = ['name', 'user__username']
admin.site.register(User, PollHistoryAdmin)