from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlateViewSet, BidViewSet, UserViewSet, register_user, home

router = DefaultRouter()
router.register('users', UserViewSet, 'users')
router.register('bids', BidViewSet, 'bids')
router.register('plates', PlateViewSet, 'plates')

urlpatterns = [
    path('home/', include(router.urls)),
    path('register/', register_user, name='register'),
    path('', home, name='home'),
]