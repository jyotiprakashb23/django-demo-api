from django.urls import path
from .views import PlotBookView, PlotListCreateView, PlotDetailView

urlpatterns = [
    path('plots/', PlotListCreateView.as_view(), name='plot-list'),
    path('plots/<int:pk>/', PlotDetailView.as_view(), name='plot-detail'),
    path('plots/<int:id>/book/', PlotBookView.as_view(), name='plot-book'),
]