from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings

class CustomUser(AbstractUser):
    number = models.CharField(max_length=20,blank=True)
    user_type = models.CharField(max_length=1000,blank=True,default='user')
    profile_pic = models.TextField(blank=True,null=True)
    lat = models.FloatField(null=True, blank=True)
    lon = models.FloatField(null=True, blank=True)
    deleted=models.BooleanField(default=False)
    lastseen = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',  # Custom related_name
        blank=True,
        verbose_name='groups',
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
    )
    # Add related_name for user_permissions
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',  # Custom related_name
        blank=True,
        verbose_name='user permissions',
        help_text='Specific permissions for this user.',
    )

class Post(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='posts',
        null=True,
        blank=True
    ) 
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    deleted=models.BooleanField(default=False)
    location = models.CharField(max_length=255)
    shared = models.BooleanField(default=False)
    sharer_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='shared_posts',
        null=True,
        blank=True
    ) 
    comment = models.BooleanField(default=True)
    def __str__(self):
        return self.title

class Image(models.Model):
    img_url = models.TextField(blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return self.img_url

class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='comments' 
    )
    comment_text = models.TextField()
    deleted=models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user_id = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='commented_posts',
        null=True,
        blank=True
    )
    image = models.TextField()

    def __str__(self):
        return self.comment_text

class ResponseComment(models.Model):
    post_id = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
    text = models.TextField()
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    img = models.TextField(null=True)

    def __str__(self):
        return self.text


class Like(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    liked = models.BooleanField(default=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} likes {self.post}"


class Tag(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    text = models.CharField(max_length=255)
    data = models.CharField(max_length=100,blank=False,null=True)
    icon = models.CharField(max_length=100)
    color = models.CharField(max_length=100,default='#eee')
    
    def __str__(self):
        return self.text

class UserTag(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    deleted = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.tag.text}"