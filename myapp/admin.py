from django.contrib import admin
from .models import Problems_section
from django.contrib.sessions.models import Session
from accounts.models import User


class CustomSessionAdmin(admin.ModelAdmin):
    list_display = ('user', 'expire_date')

    def user(self, obj):
        # Get the associated user for the session
        user_id = obj.get_decoded().get('_auth_user_id')
        if user_id:
            return User.objects.get(pk=user_id)
        return None
    user.short_description = 'Username'


admin.site.register(Session, CustomSessionAdmin)


admin.site.register(Problems_section)
