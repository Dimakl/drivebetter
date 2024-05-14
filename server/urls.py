from django.urls import path
from server.views.views import (
    LocationDataView,
    BatchLocationDataView,
    LocationCheckDataView,
    RideDataView
)
from server.views.login_views import LoginView
from server.views.profile_views import ProfileDataView

urlpatterns = [
    path('location', LocationDataView.as_view()),
    path('location/check', LocationCheckDataView.as_view()),
    path('location/batch', BatchLocationDataView.as_view()),
    path('profile', ProfileDataView.as_view()),
    path('ride', RideDataView.as_view()),
    path('login', LoginView.as_view())
]
{
    "status": "200 OK",
    "token": "string"
}
