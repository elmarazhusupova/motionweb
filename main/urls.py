from django.urls import path, include
from rest_framework import routers
from .views import *


router = routers.DefaultRouter()
router.register(r'courses', CourseView)
router.register(r'application', ApplicationView)
router.register(r'feedback', FeedbackView)

urlpatterns = [
    path('', include(router.urls)),
]
