from django.contrib import admin

from apps.lettings.models import Letting
from apps.lettings.models import Address
from .models import Profile


admin.site.register(Letting)
admin.site.register(Address)
admin.site.register(Profile)
