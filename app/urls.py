from django.urls import path

from app.views import ComicRating

urlpatterns = [
	# path("ratings/"),
	path("comics/<int:comic_id>/rating/", ComicRating.as_view({"get": "list"}))]
