from django.urls import path

from .views import OwnerCreateView, LocalCreateViewRemove, EnviromentCreateViewRemove, DeviceCreateViewRemove, DeviceOnOffLine, DeviceOnOff, DeviceOnOffLineById, DeviceOnOffById, LocalTurnOnOffDevices, LocalTurnOnOffLineDevices


urlpatterns = [
    path('owner/', OwnerCreateView.as_view(), name = 'owner_create'),
    path('owner/<int:owner_id>', OwnerCreateView.as_view(), name = 'owner_view'),
    path('owner/<int:owner_id>/local/', LocalCreateViewRemove.as_view(), name = 'local_create'),
    path('owner/<int:owner_id>/local/<int:local_id>', LocalCreateViewRemove.as_view(), name = 'local_view_delete'),
    path('owner/<int:owner_id>/local/<int:local_id>/turn_offon/<int:wish>', LocalTurnOnOffDevices.as_view(), name = 'local_turn_on_off_devices'),
    path('owner/<int:owner_id>/local/<int:local_id>/turn_offonline/<int:wish>', LocalTurnOnOffLineDevices.as_view(), name = 'local_turn_on_off_line_devices'),
    path('owner/<int:owner_id>/local/<int:local_id>/enviroment/', EnviromentCreateViewRemove.as_view(), name = 'enviroment_create'),
    path('owner/<int:owner_id>/local/<int:local_id>/enviroment/<int:enviroment_id>', EnviromentCreateViewRemove.as_view(), name = 'enviroment_view_delete'),
    path('owner/<int:owner_id>/local/<int:local_id>/enviroment/<int:enviroment_id>/device/', DeviceCreateViewRemove.as_view(), name = 'device_create'),
    path('owner/<int:owner_id>/local/<int:local_id>/enviroment/<int:enviroment_id>/device/<int:device_id>', DeviceCreateViewRemove.as_view(), name = 'device_view_delete'),
    path('owner/<int:owner_id>/local/<int:local_id>/enviroment/<int:enviroment_id>/device/turn_offon/<int:wish>', DeviceOnOff.as_view(), name = 'devices_turn_on_off'),
    path('owner/<int:owner_id>/local/<int:local_id>/enviroment/<int:enviroment_id>/device/turn_offonline/<int:wish>', DeviceOnOffLine.as_view(), name = 'devices_turn_on_off_line'),
    path('owner/<int:owner_id>/local/<int:local_id>/enviroment/<int:enviroment_id>/device/<int:device_id>/turn_offon/<int:wish>', DeviceOnOffById.as_view(), name = 'devices_turn_on_off_by_id'),
    path('owner/<int:owner_id>/local/<int:local_id>/enviroment/<int:enviroment_id>/device/<int:device_id>/turn_offonline/<int:wish>', DeviceOnOffLineById.as_view(), name = 'devices_turn_on_off_line_by_id'),
]