from django.contrib import admin
from django.contrib.auth.models import Group

from .models import AdvUser, DocsFile, SendedDocs


admin.site.unregister(Group)

admin.site.register(AdvUser)
admin.site.register(DocsFile)
admin.site.register(SendedDocs)
