from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PlateViewSet, BidViewSet, UserViewSet, register_view, home, place_bid, login_view, logout_view, update_bid, delete_bid

router = DefaultRouter()
router.register('users', UserViewSet, 'users')
router.register('bids', BidViewSet, 'bids')
router.register('plates', PlateViewSet, 'plates')

urlpatterns = [
    path('home/', include(router.urls)),
    path('register/', register_view, name='register'),
    path('', home, name='home'),
    path('place_bid/<int:plate_id>/', place_bid, name='place_bid'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('update/<int:bid_id>', update_bid, name='update_bid'),
    path('delete/<int:bid_id>', delete_bid, name='delete_bid'),
]