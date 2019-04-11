from django.urls import path
from doors.views import DoorsListView, DoorDetailView


urlpatterns = [
    path('', DoorsListView.as_view()),
    path(
        'doors/<int:pk>/<int:picture_pk>/',
        DoorDetailView.as_view(),
        name='door_detail'),
]
