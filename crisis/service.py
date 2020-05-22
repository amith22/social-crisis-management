from crisis.beans import PostBean
from crisis.eventfilter import isCrisisPost
from crisis.models import LikeOrDisLikeModel, CommentModel, PostModel, ShareModel, FriendRequestModel
from crisis.sentimentanalyzer import getCommentSentiment


def getPostBeanById(postid):

    post=PostModel.objects.get(id=postid)

    post.image = str(post.image).split("/")[1]
    comments = CommentModel.objects.filter(post=post.id)

    positive = 0
    negative = 0
    neutral = 0

    for comment in comments:

        centiment = getCommentSentiment(comment.comment)

        if centiment == 'positive':
            positive = positive + 1

        if centiment == 'negative':
            negative = negative + 1

        if centiment == 'neutral':
            neutral = neutral + 1

    likes = 0
    dislikes = 0

    for likeordislike in LikeOrDisLikeModel.objects.filter(post=post.id):

        if int(likeordislike.status) == 0:
            dislikes = dislikes + 1
        elif int(likeordislike.status) == 1:
            likes = likes + 1

    return PostBean(post, comments, likes, dislikes, positive, negative, neutral)

def getAllPosts():

    posts = []

    for post in PostModel.objects.all().order_by('-datetime'):
        posts.append(getPostBeanById(post.id))

    finalposts = []

    for postbean in posts:
        res = isCrisisPost(postbean.post.title)
        if res[0] == False:
            finalposts.append(postbean)

    return finalposts

def getAllPostsByUser(username):

    posts = []

    friends=getMyFriends(username)
    friends.add(username)

    friends=list(friends)

    print("users", friends)

    for post in PostModel.objects.filter(username__in=friends).order_by('-datetime'):
        print("posts", friends)
        posts.append(getPostBeanById(post.id))

    for share in ShareModel.objects.filter(username__in=friends):
        print("shares", friends)
        posts.append(getPostBeanById(share.post))

    finalposts=[]

    for postbean in posts:
        res = isCrisisPost(postbean.post.title)
        if res[0] == False:
            finalposts.append(postbean)

    return finalposts

def getAllPostsBySearch(keyword):

    posts = []

    for post in PostModel.objects.order_by('-datetime'):
        if keyword in post.title or keyword in post.username:
            posts.append(getPostBeanById(post.id))

    finalposts = []

    for postbean in posts:
        res = isCrisisPost(postbean.post.title)
        if res[0] == False:
            finalposts.append(postbean)

    return finalposts

def getMyFriends(username):

    friends=set()

    for request in FriendRequestModel.objects.filter(username=username,status="yes"):
        friends.add(request.friendname)

    for request in FriendRequestModel.objects.filter(friendname=username,status="yes"):
        friends.add(request.username)

    return friends