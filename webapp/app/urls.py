from django.urls import path
from . import views

app_name = 'app' 

urlpatterns = [
    path('list/', views.AppListView.as_view(), name='list'), 
    path('detail/<int:pk>/', views.AppDetailView.as_view(), name='detail'), 
    path('create/', views.AppCreateView.as_view(), name='create'), 
    path('update/<int:pk>/', views.AppUpdateView.as_view(), name='update'), 
    path('delete/<int:pk>/', views.AppDeleteView.as_view(), name='delete'), 
]










"""
urlpatterns = [
    path('app/', views.ListAppView.as_view(), name='list-app'),
    path('app/<int:pk>/detail/', views.DetailAppView.as_view(),name='detail-app'),
    path('app/create/', views.CreateAppView.as_view(), name='create-app'),
    path('app/<int:pk>/delete/', views.DeleteAppView.as_view(),name='delete-app'),
    path('app/<int:pk>/update/', views.UpdateAppView.as_view(),name='update-app')
]
"""