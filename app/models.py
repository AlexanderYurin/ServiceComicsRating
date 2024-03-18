from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
"""Создайте модель Comic с полями:
 
id (уникальный идентификатор)
title (название комикса)
author (автор комикса)
rating (рейтинг комикса, по умолчанию 0)
Создайте модель Rating с полями:
 
id (уникальный идентификатор)
comic_id (ссылка на комикс)
user_id (идентификатор пользователя, оценившего комикс)
VALUE (оценка пользователя от 1 до 5)
Реализуйте API endpoint для создания оценки комикса:"""


class Comic(models.Model):
	title = models.CharField(max_length=50)
	author = models.CharField(max_length=50)
	total_rating = models.PositiveIntegerField(default=0)


class Rating(models.Model):
	comic_id = models.ForeignKey(to=Comic, on_delete=models.CASCADE, related_name="rating")
	user_id = models.IntegerField()
	value = models.PositiveIntegerField(default=1, validators=[MinValueValidator(1), MaxValueValidator(5)])
