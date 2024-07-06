from rest_framework.routers import SimpleRouter
from .views import PostViewSet, UserViewset


router = SimpleRouter()
router.register('users', UserViewset, basename='users')
router.register('', PostViewSet, basename='posts')

urlpatterns = router.urls