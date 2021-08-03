from django.urls import path
import authapp.views as views


urlpatterns = [
    path('', views.UserApiView.as_view()),
    path('<int:pk>', views.UserApiView.as_view()),
]
