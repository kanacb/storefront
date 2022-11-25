from django.urls import path
from . import views

urlpatterns = [
    path('products/', views.ProdustListView.as_view() ),
    path('product/<int:id>/',views.ProdustListView.as_view()),
]
