# queryset_exclude.py
from articles.models import Article

# 게시글을 작성한 고유 사용자 ID 목록
author_ids = Article.objects.values_list('author', flat=True).distinct()
print(f"게시글을 작성한 고유 사용자 수: {len(author_ids)}")
