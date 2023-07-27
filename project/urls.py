import os

from django.conf import settings
from django.contrib import admin
from django.urls import path

urlpatterns = []

if settings.DEBUG:
    urlpatterns += [
        path("admin/", admin.site.urls),
    ]
else:
    urlpatterns += [
        path(
            "admin/" + os.getenv("ADMIN_PREFIX", default="test/"),
            admin.site.urls,
        ),
    ]
