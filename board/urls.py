from rest_framework.router import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'sprints', views.SprintViewsSet)
router.register(r'task', views.TaskViewSet)
router.register(r'users', views.UserViewSet)
