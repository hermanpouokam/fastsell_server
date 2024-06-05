
from django.urls import path
from .views import UserListCreateView, UserRetrieveUpdateDestroyView,PostListCreateView, PostRetrieveUpdateDestroyView,ImageListCreateView,ImageRetrieveUpdateDestroyView,PostImagesListView,CommentListCreateView,CommentRetrieveUpdateDestroyView,ResponseCommentListCreateView,ResponseCommentRetrieveUpdateDestroyView,LikeListCreateView,LikeRetrieveUpdateDestroyView,TagListCreateView,TagRetrieveUpdateDestroyView,UserTagListCreateView,UserTagRetrieveUpdateDestroyView
from .functions import get_post_comments,get_comment_responses,get_user_posts,get_post_likes,get_user_tag_list

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('users/<int:id>/', UserRetrieveUpdateDestroyView.as_view(), name='user-detail-update-delete'),
    path('posts/', PostListCreateView.as_view(), name='post-list-create'),
    path('posts/<int:post_id>/', PostRetrieveUpdateDestroyView.as_view(), name='post-detail-update-delete'),
    path('images/', ImageListCreateView.as_view(), name='image-list-create'),
    path('images/<int:id>/', ImageRetrieveUpdateDestroyView.as_view(), name='image-detail-update-delete'),
    path('posts/<int:post_id>/images/', PostImagesListView.as_view(), name='post-images-list'),
    path('comments/', CommentListCreateView.as_view(), name='comment-list-create'),
    path('comments/<int:id>/', CommentRetrieveUpdateDestroyView.as_view(), name='comment-detail-update-delete'),
    path('posts/<int:post_id>/comments/', get_post_comments, name='post-comments'),
    path('response-comments/', ResponseCommentListCreateView.as_view(), name='response-comment-list-create'),
    path('response-comments/<int:id>/', ResponseCommentRetrieveUpdateDestroyView.as_view(), name='response-comment-detail-update-delete'),
    path('comments/<int:comment_id>/responses/', get_comment_responses, name='comment-responses'),
    path('users/<int:user_id>/posts/', get_user_posts, name='user-posts'),
    path('likes/', LikeListCreateView.as_view(), name='like-list-create'),
    path('likes/<int:id>/', LikeRetrieveUpdateDestroyView.as_view(), name='like-retrieve-update-destroy'),
    path('posts/<int:post_id>/likes/', get_post_likes, name='post-likes'),
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),
    path('tags/<int:id>/', TagRetrieveUpdateDestroyView.as_view(), name='tag-retrieve-update-destroy'),
    path('user-tags/', UserTagListCreateView.as_view(), name='user-tag-list-create'),
    path('user-tags/<int:id>/', UserTagRetrieveUpdateDestroyView.as_view(), name='user-tag-retrieve-update-destroy'),
    path('users/<int:user_id>/user-tags/', get_user_tag_list, name='user-tags-list'),
]
