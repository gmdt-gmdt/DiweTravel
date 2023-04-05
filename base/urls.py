from django.urls import path
from . import views


urlpatterns = [

    path('delete/<str:pk>/', views.deleteUser, name='user-delete'),

    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),

    path('register/', views.registerUser, name='register'),

    path('profile/', views.getUserProfile, name="users-profile"),

    path('<str:pk>/', views.getUserById, name='user'),

    path('update/<str:pk>/', views.updateUser, name='user-update'),

    path('profile/update/', views.updateUserProfile, name="user-profile-update"),

    path('', views.getUsers, name="users"),
]
