from django.test import TestCase

from rest_framework.test import APIClient
from rest_framework import status
from app.models import Comic, Rating


class RatingAPITest(TestCase):
	def setUp(self):
		self.comic1 = Comic.objects.create(title="Comic 1", author="Author 1")
		self.comic2 = Comic.objects.create(title="Comic 2", author="Author 2")
		self.client = APIClient()

	def test_create_rating(self):
		data = {"comic_id": self.comic1.id, "user_id": 1, "value": 4}
		response = self.client.post("/api/ratings/", data, format="json")
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		comic = Comic.objects.get(pk=self.comic1.id)
		self.assertEqual(comic.total_rating, 4.0)

	def test_update_rating(self):
		Rating.objects.create(comic_id=self.comic2, user_id=1, value=3)

		data = {"comic_id": self.comic2.id, "user_id": 1, "value": 5}
		response = self.client.post("/api/ratings/", data, format="json")
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		comic = Comic.objects.get(pk=self.comic2.id)
		self.assertEqual(comic.total_rating, 5.0)

	def test_avg_rating(self):
		for i in range(1, 6):
			data = {"comic_id": self.comic2.id, "user_id": i, "value": i}
			response = self.client.post("/api/ratings/", data, format="json")
			self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		comic = Comic.objects.get(pk=self.comic2.id)
		self.assertEqual(comic.total_rating, sum(range(1, 6)) / 5)

	def test_invalid_rating(self):
		data = {"comic_id": self.comic1.id, "user_id": 1, "value": 6}
		response = self.client.post("/api/ratings/", data, format="json")
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
