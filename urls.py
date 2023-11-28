from django.urls import path, include
# from rest_framework.routers import DefaultRouter
from .views import OwnerCreateView, LocalCreateViewRemove, EnviromentCreateViewRemove, DeviceCreateViewRemove

# owner_router = DefaultRouter()
# owner_router.register(r'owner', OwnerCreate, basename = 'owner')

# local_router = DefaultRouter()
# local_router.register(r'local', LocalViewSet, basename = 'local')

# enviroment_router = DefaultRouter()
# enviroment_router.register(r'enviroment', EnviromentViewSet, basename = 'enviroment')

# device_router = DefaultRouter()
# device_router.register(r'device', DeviceViewSet, basename = 'device')

urlpatterns = [
    path('owner/', OwnerCreateView.as_view(), name = 'owner_create'),
    path('owner/<int:owner_id>', OwnerCreateView.as_view(), name = 'owner_view'),
    path('owner/<int:owner_id>/local/', LocalCreateViewRemove.as_view(), name = 'local_create'),
    path('owner/<int:owner_id>/local/<int:local_id>', LocalCreateViewRemove.as_view(), name = 'local_view_delete'),
    path('owner/<int:owner_id>/local/<int:local_id>/enviroment/', EnviromentCreateViewRemove.as_view(), name = 'enviroment_create'),
    path('owner/<int:owner_id>/local/<int:local_id>/enviroment/<int:enviroment_id>', EnviromentCreateViewRemove.as_view(), name = 'enviroment_view_delete'),
    path('owner/<int:owner_id>/local/<int:local_id>/enviroment/<int:enviroment_id>/device/', DeviceCreateViewRemove.as_view(), name = 'device_create'),
    path('owner/<int:owner_id>/local/<int:local_id>/enviroment/<int:enviroment_id>/device/<int:device_id>', DeviceCreateViewRemove.as_view(), name = 'device_view_delete'),
    # path('owner/<int:owner_id>/', include(owner_router.urls)),
    # path('owner/<int:owner_id>/local/<int:local_id>/', include(local_router.urls)),
    # path('owner/<int:owner_id>/local/<int:local_id>/enviroment/<int:enviroment_id>/', include(enviroment_router.urls)),
    # path('owner/<int:owner_id>/local/<int:local_id>/enviroment/<int:enviroment_id>/device/<int:device_id>', include(device_router.urls)),
]