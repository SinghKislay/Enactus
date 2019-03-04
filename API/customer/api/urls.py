from django.urls import path

from .views import(
    UserCreateAPIView,
    UserLoginAPIView,
    DataManView,
    DataUpdateView
)

urlpatterns=[
    path('register/',UserCreateAPIView.as_view(),name="register"),
    path('login/',UserLoginAPIView.as_view(),name="login"),
    path('data/',DataManView.as_view(),name="data_fetch"),
    path('update_data/',DataUpdateView.as_view(),name="update_data")
]