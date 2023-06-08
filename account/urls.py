from django.urls import path
from .views import UserListView, UserDetailView

urlpatterns = [
    path('', UserListView.as_view(), name='users_url'),
    path('<int:user_id>', UserDetailView.as_view(), name='user_url'),
]
