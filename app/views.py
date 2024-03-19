from django.db.models import Avg
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ViewSet

from app.models import Comic, Rating
from app.serializers import ComicSerializer, RatingSerializer


class RatingViewSet(ViewSet):
	def create(self, request):

		serializer = RatingSerializer(data=request.data)
		if serializer.is_valid():

			comic_id = serializer.validated_data["comic_id"]
			user_id = serializer.validated_data["user_id"]
			value = serializer.validated_data["value"]

			rating = Rating.objects.filter(comic_id_id=comic_id, user_id=user_id)
			if rating.exists():
				rating.update(value=value)
			else:
				rating.create(comic_id_id=comic_id, user_id=user_id, value=value)

			comic = Comic.objects.filter(pk=comic_id).annotate(avg_rating=Avg("rating__value")).first()
			comic.total_rating = comic.avg_rating
			comic.save()

			return Response({"message": "Rating created successfully"}, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ComicRating(ReadOnlyModelViewSet):
	queryset = Comic.objects.all()
	serializer_class = ComicSerializer
