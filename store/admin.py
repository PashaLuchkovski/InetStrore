from django.contrib import admin
from store.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('lastName','firstName','login')

admin.site.register(User, UserAdmin)