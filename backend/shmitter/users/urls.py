from rest_framework.routers import DefaultRouter

from shmitter.users.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = router.urls
