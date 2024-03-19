from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.


class Comic(models.Model):
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	total_rating = models.FloatField(default=0.0)


class Rating(models.Model):
	comic_id = models.ForeignKey(to=Comic, on_delete=models.CASCADE, related_name="rating")
	user_id = models.IntegerField()
	value = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
