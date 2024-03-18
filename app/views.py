
from rest_framework.viewsets import ReadOnlyModelViewSet

from app.models import Comic
from app.serializers import ComicRatingSerializer


# Create your views here.


class CreateRating():
	pass


class ComicRating(ReadOnlyModelViewSet):
	queryset = Comic.objects.all()
	serializer_class = ComicRatingSerializer