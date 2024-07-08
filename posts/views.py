from django.contrib.auth import get_user_model
from rest_framework import viewsets, filters
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, UserSerializer

# Create your views here.

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    search_fields = ['title','body']
    ordering_fields = ['created_at']
    filter_backends = (filters.SearchFilter,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    
class UserViewset(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer