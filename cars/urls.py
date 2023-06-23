# from django.contrib import admin
# from django.urls import path, include

# urlpatterns = [
#     path('', include('cars.urls')),
#     path('admin/', admin.site.urls),
# ]


from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.CarListView.as_view(), name='all'),
    path('cars/<int:pk>/detail/', views.CarDetailView.as_view(), name='car_detail'),
    path('cars/create/', views.CarCreateView.as_view(), name='car_create'),
    path('cars/<int:pk>/update/', views.CarUpdateView.as_view(), name='car_update'),
    path('cars/<int:pk>/delete/', views.CarDeleteView.as_view(), name='car_delete'),
    path('cars/update/bulk/', views.update_cars_view),
    path('api/colors/', views.get_colors),
    path('api/brands/', views.get_brands),
    path('api/cars/', views.get_cars),
    path('api/cars/update/bulk/', views.update_cars),
]
