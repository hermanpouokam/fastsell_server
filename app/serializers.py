from rest_framework import serializers
from .models import CustomUser,Post,Image,Comment,ResponseComment,Like,Tag,UserTag,Follower



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
    
class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['post_id','user', 'title', 'description', 'price', 'location','deleted', 'shared', 'sharer_user', 'comment']

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ['id', 'img_url', 'post']

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'post', 'comment_text', 'created_at', 'user_id','deleted']

class ResponseCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResponseComment
        fields = ['id', 'post_id', 'comment', 'text', 'created_at', 'user', 'img','deleted']
    
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ['user', 'created_at', 'liked', 'post']
    
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