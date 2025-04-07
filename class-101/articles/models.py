from django.conf import settings
from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils.models import UUIDModel, SoftDeletableModel, TimeStampedModel

class Article(UUIDModel, SoftDeletableModel, TimeStampedModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='articles',
        verbose_name='author'
    )
    title = models.CharField(max_length=255, verbose_name='title')
    content = models.TextField(verbose_name='content')
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    @property
    def like_count(self):
        """게시글의 좋아요 수를 반환합니다."""
        return self.likes.count()

    @property
    def comment_count(self):
        """게시글의 댓글 수를 반환합니다."""
        return self.comments.count()

    def is_liked_by(self, user):
        """특정 사용자가 게시글에 좋아요를 눌렀는지 확인합니다."""
        return self.likes.filter(user=user).exists()