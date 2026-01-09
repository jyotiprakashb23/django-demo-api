from django.urls import path
from .views import NoteListCreateView, NoteDelete, NoteDetailUpdateView

urlpatterns = [
    path('create-list-notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('delete-note/<int:pk>/', NoteDelete.as_view(), name='note-delete'),
    path('detail-update-note/<int:pk>/', NoteDetailUpdateView.as_view(), name='note-detail-update'),
]