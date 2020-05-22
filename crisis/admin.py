from django.contrib import admin

# Register your models here.
from crisis.models import RegistrationModel, PostModel, CommentModel, LikeOrDisLikeModel, ShareModel, \
    FriendRequestModel, PoliceModel, EventModel

admin.site.register(RegistrationModel)
admin.site.register(PostModel)
admin.site.register(CommentModel)
admin.site.register(LikeOrDisLikeModel)
admin.site.register(ShareModel)
admin.site.register(FriendRequestModel)
admin.site.register(PoliceModel)
admin.site.register(EventModel)