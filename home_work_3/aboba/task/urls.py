from django.urls import path
from . import views

urlpatterns = [
    path("admin_panel/", views.admin_panel, name="admin_panel"),
    path("admin_panel/add_user/", views.add_user, name="add_user"),
    path("admin_panel/del_user/", views.del_user, name="del_user"),
]
