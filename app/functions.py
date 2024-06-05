from django.shortcuts import get_object_or_404
from .models import Comment,ResponseComment,CustomUser,Like,UserTag
from .serializers import CommentSerializer,ResponseCommentSerializer,PostSerializer,LikeSerializer,UserTagSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Post

@api_view(['GET'])
def get_post_comments(request, post_id):
    post = get_object_or_404(Post, post_id=post_id)
    comments = Comment.objects.filter(post=post)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_comment_responses(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    responses = ResponseComment.objects.filter(comment=comment)
    serializer = ResponseCommentSerializer(responses, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_posts(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    posts = Post.objects.filter(user_id=user_id)
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_post_likes(request, post_id):
    likes = Like.objects.filter(post_id=post_id, liked=True)
    serializer = LikeSerializer(likes, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_user_tag_list(request, user_id):
    user_tags = UserTag.objects.filter(user_id=user_id)
    serializer = UserTagSerializer(user_tags, many=True)
    return Response(serializer.data)