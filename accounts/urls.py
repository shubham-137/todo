from django.urls import path
from . import views


urlpatterns = [
	# path('', views.todo_view, name="todo-view"),
    path('', views.register, name="register"),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
]
