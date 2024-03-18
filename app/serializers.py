from django.db.migrations import serializer

from app.models import Comic


class ComicRatingSerializer(serializer.ModelFieldSerializer):
	class Meta:
		model = Comic
		fields = ("__all__",)