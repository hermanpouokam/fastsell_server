from rest_framework import serializers
from .models import CustomUser,Post,Image,Comment,ResponseComment,Like,Tag,UserTag



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'first_name', 'user_type', 'profile_pic','last_name', 'email', 'password', 'number','deleted', 'lat', 'lon', 'lastseen', 'created_at', 'updated_at']
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