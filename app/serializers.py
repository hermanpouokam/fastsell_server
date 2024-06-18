from rest_framework import serializers
from .models import (CustomUser,Post,Image,Comment,ResponseComment,Like,Tag,UserTag,Follower,ViewedPost,FavoriteUserPost,
                     LikeCommentResponse
                     )
from django.contrib.contenttypes.models import ContentType


class CustomUserSerializer(serializers.ModelSerializer):

    followers = serializers.SerializerMethodField()
    following = serializers.SerializerMethodField()

    def get_followers(self, obj):
        followers = Follower.objects.filter(user=obj, following=True)
        return FollowerSerializer(followers, many=True).data

    def get_following(self, obj):
        following = Follower.objects.filter(follower=obj, following=True)
        return FollowerSerializer(following, many=True).data
    
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'user_type', 'profile_pic','last_name', 'email','is_certified', 'is_verified','password', 'number','deleted', 'lat', 'lon','bio', 'cover_pic', 'lastseen', 'created_at', 'updated_at','uid','is_first_login','followers', 'following']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = CustomUser.objects.create_user(**validated_data)
        return user
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance
    
class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'img_url', 'post']

class CommentSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()
    responses = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ['id', 'post', 'comment_text', 'created_at', 'user_id', 'deleted', 'likes','responses',]

    def get_likes(self, obj):
        content_type = ContentType.objects.get_for_model(Comment)
        likes = LikeCommentResponse.objects.filter(content_type=content_type, object_id=obj.id)
        return LikeResponseCommentSerializer(likes, many=True).data
    def get_responses(self, obj):
        responses = ResponseComment.objects.filter(comment=obj)
        serializer = ResponseCommentSerializer(responses, many=True)
        return serializer.data

class ResponseCommentSerializer(serializers.ModelSerializer):
    likes = serializers.SerializerMethodField()

    class Meta:
        model = ResponseComment
        fields = ['id', 'post_id', 'comment', 'text', 'created_at', 'user', 'img', 'deleted', 'likes']

    def get_likes(self, obj):
        content_type = ContentType.objects.get_for_model(ResponseComment)
        likes = LikeCommentResponse.objects.filter(content_type=content_type, object_id=obj.id)
        return LikeResponseCommentSerializer(likes, many=True).data

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    response_comments = ResponseCommentSerializer(many=True, read_only=True)
    likes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['post_id', 'user', 'title', 'description', 'price', 'location', 'deleted', 'shared', 'sharer_user',
                  'comment', 'created_at', 'updated_at', 'selled', 'comments', 'response_comments', 'likes']

    def get_likes(self, obj):
        likes = Like.objects.filter(post=obj)
        return LikeSerializer(likes, many=True).data
    
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['id','user', 'created_at', 'liked', 'post']
    
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['user', 'created_at', 'text', 'icon','color','data']

class UserTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserTag
        fields = ['user', 'tag', 'created_at', 'deleted']
    
class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ['id', 'user', 'follower', 'followed_at', 'updated_at', 'following']

class ViewedPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = ViewedPost
        fields = ['user', 'post', 'created_at'] 
    
class FavoriteUserPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteUserPost
        fields = ['id', 'user', 'post', 'created_at']

class LikeResponseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeCommentResponse
        fields = ['id', 'user', 'created_at', 'liked', 'content_type', 'object_id']