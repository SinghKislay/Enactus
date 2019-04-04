from django.urls import path

from .views import(
    UserCreateAPIView,
    UserLoginAPIView,
    DataManView,
    DataUpdateView,
    ServiceView,
    EmployeeView,
)

urlpatterns=[
    path('register/',UserCreateAPIView.as_view(),name="register"),
    path('login/',UserLoginAPIView.as_view(),name="login"),
    path('data/',DataManView.as_view(),name="data_fetch"),
    path('update_data/',DataUpdateView.as_view(),name="update_data"),
    path('service_request/',ServiceView.as_view(),name='service'),
    path('employee_request/',EmployeeView.as_view(),name='employee'),
]