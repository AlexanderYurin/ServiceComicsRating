from django.core.validators import MinValueValidator, MaxValueValidator
from rest_framework import serializers

from app.models import Comic


class ComicSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comic
		fields = "__all__"


class RatingSerializer(serializers.Serializer):
	comic_id = serializers.IntegerField()
	user_id = serializers.IntegerField()
	value = serializers.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])

