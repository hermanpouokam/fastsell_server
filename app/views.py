# myapp/views.py

from rest_framework import generics
from .models import CustomUser,Post,Image,Comment,ResponseComment,Like,Tag,UserTag
from .serializers import CustomUserSerializer, PostSerializer,ImageSerializer,CommentSerializer,ResponseCommentSerializer,LikeSerializer,TagSerializer,UserTagSerializer

class UserListCreateView(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer

class UserRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer
    lookup_field = 'id'

class PostListCreateView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

class PostRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'post_id'

class ImageListCreateView(generics.ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

class ImageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    lookup_field = 'id'

class PostImagesListView(generics.ListAPIView):
    serializer_class = ImageSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Image.objects.filter(post_id=post_id)

class CommentListCreateView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'post_id'

class ResponseCommentListCreateView(generics.ListCreateAPIView):
    queryset = ResponseComment.objects.all()
    serializer_class = ResponseCommentSerializer

class ResponseCommentRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = ResponseComment.objects.all()
    serializer_class = ResponseCommentSerializer
    lookup_field = 'id'


class LikeListCreateView(generics.ListCreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

class LikeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    lookup_field = 'id'

class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class TagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    lookup_field = 'id'


class UserTagListCreateView(generics.ListCreateAPIView):
    queryset = UserTag.objects.all()
    serializer_class = UserTagSerializer

class UserTagRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserTag.objects.all()
    serializer_class = UserTagSerializer
    lookup_field = 'id'