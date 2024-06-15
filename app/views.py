# myapp/views.py

from rest_framework import generics
from .models import CustomUser,Post,Image,Comment,ResponseComment,Like,Tag,UserTag,Follower,ViewedPost
from .serializers import CustomUserSerializer, PostSerializer,ImageSerializer,CommentSerializer,ResponseCommentSerializer,LikeSerializer,TagSerializer,UserTagSerializer,ViewedPostSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

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

class FollowerToggleAPIView(APIView):
    def post(self, request, id):
        user_id = id  # Use the `id` captured from URL path
        data = request.data  # Get request data
        
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            return Response({"detail": "User with id {} does not exist.".format(user_id)}, status=status.HTTP_404_NOT_FOUND)

        # For simplicity, assuming follower ID is provided in request data
        follower_id = data.get('follower_id', None)

        if not follower_id:
            return Response({"detail": "follower_id is required in request data."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            follower = CustomUser.objects.get(id=follower_id)
        except CustomUser.DoesNotExist:
            return Response({"detail": "Follower with id {} does not exist.".format(follower_id)}, status=status.HTTP_404_NOT_FOUND)

        if user_to_follow == follower:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            # Check if the follower relationship already exists
            follower_relationship, created = Follower.objects.get_or_create(user=user_to_follow, follower=follower)
            # Toggle the following status
            follower_relationship.following = not follower_relationship.following
            follower_relationship.save()
            
            serializer = CustomUserSerializer(user_to_follow)  # Serialize the user being followed/unfollowed
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Follower.DoesNotExist:
            return Response({"detail": "Failed to toggle follow status."}, status=status.HTTP_400_BAD_REQUEST)




class ViewedPostCreateAPIView(generics.CreateAPIView):
    queryset = ViewedPost.objects.all()
    serializer_class = ViewedPostSerializer

    def create(self, request, *args, **kwargs):
        user_id = request.data.get('user')
        post_id = request.data.get('post')

        if not user_id or not post_id:
            return Response({"detail": "user and post fields are required."}, status=status.HTTP_400_BAD_REQUEST)

        try:
            user = CustomUser.objects.get(id=user_id)
            post = Post.objects.get(post_id=post_id)
        except CustomUser.DoesNotExist:
            return Response({"detail": "User does not exist."}, status=status.HTTP_400_BAD_REQUEST)
        except Post.DoesNotExist:
            return Response({"detail": "Post does not exist."}, status=status.HTTP_400_BAD_REQUEST)

        viewed_post, created = ViewedPost.objects.get_or_create(user=user, post=post)

        if created:
            return Response({"detail": "ViewedPost created successfully."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "ViewedPost already exists."}, status=status.HTTP_200_OK)

class UsersWhoViewedPostAPIView(APIView):
    def get(self, request, post_id):
        user_ids = ViewedPost.objects.filter(post_id=post_id).values_list('user_id', flat=True)
        users = CustomUser.objects.filter(id__in=user_ids)
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)
    

class PostsNotViewedByUserAPIView(APIView):
    def get(self, request, user_id):
        viewed_post_ids = ViewedPost.objects.filter(user_id=user_id).values_list('post_id', flat=True)
        posts_not_viewed = Post.objects.exclude(post_id__in=viewed_post_ids)
        serializer = PostSerializer(posts_not_viewed, many=True)
        return Response(serializer.data)
    
class PostsViewedByUserAPIView(APIView):
    def get(self, request, user_id):
        viewed_post_ids = ViewedPost.objects.filter(user_id=user_id).values_list('post_id', flat=True)
        posts_viewed = Post.objects.filter(post_id__in=viewed_post_ids)
        serializer = PostSerializer(posts_viewed, many=True)
        return Response(serializer.data)

class UsersWhoViewedPostAPIView(APIView):
    def get(self, request, post_id):
        user_ids = ViewedPost.objects.filter(post_id=post_id).values_list('user_id', flat=True)
        users = CustomUser.objects.filter(id__in=user_ids)
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)