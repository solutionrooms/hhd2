from django.urls import path

from .views import patient_list, measurement_list, \
    add_measurement, patient_create, \
    patient_update, register, LoginView

from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView

urlpatterns = [
    path('', RedirectView.as_view(url='patients/', permanent=True)),
    path('register/', register, name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('patients/', patient_list, name='patient_list'),
    path('patients/<int:patient_id>/', measurement_list, name='measurement_list'),
    path('patients/<int:patient_id>/add_measurement/', add_measurement, name='add_measurement'),
    path('patients/new/', patient_create, name='patient_create'),
    path('patients/<int:patient_id>/edit/', patient_update, name='patient_update'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),


]
