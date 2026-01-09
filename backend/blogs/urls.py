from django.urls import path,include
from rest_framework.routers import DefaultRouter
# from .views import BlogViewSet, CommentViewSet
from .views import BlogListCreateView, CommentListCreateView, BlogDetailView, CommentDetailView,default_view

# router = DefaultRouter()
# router.register(r'blogs', BlogViewSet)
# router.register(r'comments', CommentViewSet)

# urlpatterns = [
#     path('', include(router.urls)),
# ]

urlpatterns = [
    path('', default_view, name='default-view'),
    path('blogs/', BlogListCreateView.as_view(), name='blog-list-create'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('blogs/<int:pk>/', BlogDetailView.as_view(), name='blog-detail'),
    path('comments/<int:pk>/', CommentDetailView.as_view(), name='comment-detail'),
]