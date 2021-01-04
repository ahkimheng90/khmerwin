from django.contrib import admin

from .models import  BannerHeader, BannerFooter, BannerSidebar

admin.site.register(BannerHeader)
admin.site.register(BannerSidebar)
admin.site.register(BannerFooter)
