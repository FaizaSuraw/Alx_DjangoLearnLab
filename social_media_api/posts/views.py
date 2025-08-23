from rest_framework import viewsets, permissions, filters, generics, status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer
from notifications.models import Notification


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [filters.SearchFilter]
    search_fields = ["title", "content"]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class FeedView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        following_users = request.user.following.all()
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')
        data = [
            {
                "id": post.id,
                "title": post.title,
                "content": post.content,
                "author": post.author.id,
                "author_username": post.author.username,
                "created_at": post.created_at,
                "updated_at": post.updated_at,
            }
            for post in posts
        ]
        return Response(data)


class LikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like, created = Like.objects.get_or_create(user=request.user, post=post)

        if created:
            if post.author != request.user:
                Notification.objects.create(
                    recipient=post.author,
                    actor=request.user,
                    verb="liked your post",
                    target=post
                )
            return Response({"detail": "Post liked"}, status=status.HTTP_201_CREATED)

        return Response({"detail": "You already liked this post"}, status=status.HTTP_200_OK)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, pk):
        post = generics.get_object_or_404(Post, pk=pk)
        like = Like.objects.filter(user=request.user, post=post).first()

        if like:
            like.delete()
            return Response({"detail": "Post unliked"}, status=status.HTTP_200_OK)

        return Response({"detail": "You haven't liked this post yet"}, status=status.HTTP_400_BAD_REQUEST)
