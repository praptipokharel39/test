from django.urls import path
from app import views

urlpatterns = [
    path('' , views.index , name="index"),
    path('receipes/', views.receipes , name ="receipes"),
    path('deletereceipe/<id>/', views.delete_receipe, name="deletereceipe"),
    path('updatereceipe/<id>/', views.update_receipe, name="updatereceipe"),
]
