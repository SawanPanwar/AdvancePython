from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('Hello/', views.hello),
    path('User/<int:id>', views.user),

    path('Reg/', views.registration),
    path('update/', views.update),
    path('List/', views.search),
    path('create/', views.create_session),
    path('access/', views.access_session),
    path('destroy/', views.destroy_session),
    path('set/', views.setCookies),
    path('get/', views.getCookies),
    path('red/', views.red),
    path('dis/', views.display),
    path('edit/<int:id>', views.edit),
    path('del/<int:id>', views.delete),
    path('auth/', views.login),
]