from django.http import JsonResponse
from rest_framework import viewsets,generics

from .models import Blog, Comment
from .serializers import BlogSerializer, CommentSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response

# class BlogViewSet(viewsets.ModelViewSet):
#     queryset = Blog.objects.all()
#     serializer_class = BlogSerializer

# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
@api_view(['GET'])
def default_view(request):
    return Response({
        "blogs": "/blogs/",
        "comments": "/comments/",
        "blog_detail": "/blogs/<id>/",
        "comment_detail": "/comments/<id>/"
    })
class BlogListCreateView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk' 