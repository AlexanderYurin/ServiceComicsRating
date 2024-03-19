from django.urls import path

from app.views import ComicRating, RatingViewSet

urlpatterns = [
	path("ratings/", RatingViewSet.as_view({"post": "create"})),
	path("comics/<int:pk>/rating/", ComicRating.as_view({"get": "retrieve"})),
	path("comics", ComicRating.as_view({"get": "list"}))
]

