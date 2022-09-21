from django.urls import path,include
from . import views

app_name="accounts"

urlpatterns = [
    path('signup/',views.RegisterView.as_view(), name="signup"),
    path('api/v1/', include('djoser.urls.authtoken')),
    path('user/',views.GetProfile.as_view(), name="get_user"),
    path('users-list/',views.ProfileListView.as_view(), name="users_list")
    ]