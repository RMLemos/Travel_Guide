from django.contrib import admin
from django.urls import include, path

from rest_framework import routers
from sightseeing.api.viewsets import PlaceViewSet
from attractions.api.viewsets import MustseeViewSet
from locations.api.viewsets import AddressViewSet
from reviews.api.viewsets import CommentViewSet, RatingViewSet

router = routers.DefaultRouter()
router.register(r'place', PlaceViewSet)
router.register(r'mustsee', MustseeViewSet)
router.register(r'address', AddressViewSet)
router.register(r'comment', CommentViewSet)
router.register(r'rating', RatingViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
