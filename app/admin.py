from django.contrib import admin

from app.models import Comic, Rating


# Register your models here.

@admin.register(Comic)
class AdminComic(admin.ModelAdmin):
	pass


@admin.register(Rating)
class AdminRating(admin.ModelAdmin):
	pass