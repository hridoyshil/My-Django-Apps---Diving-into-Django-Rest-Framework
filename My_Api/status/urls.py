from django.urls import path
from .views import StatusViewset
from rest_framework.routers import DefaultRouter


# from .views import (StatusDetailUpdateDeleteView,StatusListCreateView)

# status/ -> List, Create => GET, POST
# status/<id>/ -> Details, Delete, Update => GET, DELETE, PUT/PATCH

# urlpatterns = [
#     path("status/", StatusListCreateView.as_view()),
#     path("status/<id>/", StatusDetailUpdateDeleteView.as_view()),
# ]

router = DefaultRouter()
router.register(r"status", StatusViewset, basename="status")

urlpatterns = [] + router.urls