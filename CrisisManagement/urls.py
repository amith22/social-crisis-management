from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

from crisis.views import login, registration, logout, search, postComment, likeOrDisLike, \
    addPost, getposts, deletepost, sharePost, viewfriends, searchUsers, sendFriendRequest, acceptFriendRequest, \
    updateprofile, viewprofile, unFriend, updatepic, addpolice, viewpolices, deletepolice, addevent, viewevents, \
    deleteevent

urlpatterns = [

    path('admin/', admin.site.urls),

    path('login/',TemplateView.as_view(template_name = 'index.html'),name='login'),
    path('loginaction/',login,name='loginaction'),

    path('registration/',TemplateView.as_view(template_name = 'registration.html'),name='registration'),
    path('regaction/',registration,name='regaction'),

    #path('addpost/',TemplateView.as_view(template_name = 'post.html'),name='post'),
    path('postaction/',addPost,name='post action'),

    path('getposts/',getposts,name='posts'),
    path('search/',search,name='searchposts'),
    path('postcomment/',postComment,name='postcomment'),
    path('likedislike/',likeOrDisLike,name='likedislike'),
    path('deletepost/',deletepost,name='deletepost'),
    path('sharepost/',sharePost,name='share post'),

    path('viewfriends/',viewfriends,name='transactions'),
    path('searchusers/',searchUsers,name='transactions'),

    path('sendfriendrequest/',sendFriendRequest,name='transactions'),
    path('acceptfriendrequest/',acceptFriendRequest,name='transactions'),

    path('viewprofile/',viewprofile,name='transactions'),
    path('updateprofile/',updateprofile,name='transactions'),
    path('updatepic/',updatepic,name='transactions'),
    path('unfriend/',unFriend,name='transactions'),

    path('addpolice/',TemplateView.as_view(template_name = 'addpolice.html'),name='add police'),
    path('addpoliceaction/',addpolice,name='add police action'),
    path('viewpolices/',viewpolices,name='add police action'),
    path('deletepolice/',deletepolice,name='add police action'),

    path('addevent/', TemplateView.as_view(template_name='addevent.html'), name='add event'),
    path('addeventaction/', addevent, name='add event action'),
    path('viewevents/', viewevents, name='add event action'),
    path('deleteevent/', deleteevent, name='add event action'),


    path('logout/',logout,name='logout'),
]
