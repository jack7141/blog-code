from django.conf import settings
from django.contrib.contenttypes.fields import (
    GenericForeignKey, GenericRelation,
)
from django.contrib.contenttypes.models import (
    ContentType,
)
from django.db import models
from model_utils.models import TimeStampedModel, UUIDModel, SoftDeletableModel


class Like(TimeStampedModel):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='likes')
    content_type = models.ForeignKey(ContentType,on_delete=models.CASCADE,related_name='likes')
    object_id = models.UUIDField(primary_key=False)
    content_object = GenericForeignKey('content_type','object_id')

class Comment(UUIDModel, TimeStampedModel, SoftDeletableModel):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, related_name='comments')
    object_id = models.UUIDField(primary_key=False)
    content_object = GenericForeignKey('content_type','object_id')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField(max_length=1000,verbose_name='댓글 내용')
    replies = GenericRelation('self', related_query_name='comment', related_name='comment', verbose_name='대댓글')
    likes = GenericRelation(Like, related_name='comments', verbose_name='좋아요')