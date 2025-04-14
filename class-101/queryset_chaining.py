# queryset_chaining.py
import datetime

from django.utils import timezone

from articles.models import Article

one_week_ago = timezone.now() - datetime.timedelta(days=7)

# 여러 조건을 차례로 적용
chained_query = Article.objects.filter(is_published=True).filter(created__gte=one_week_ago).exclude(title__icontains='python').order_by('-created')[:3]

print("체이닝 결과 (최근 1주일 내 발행된, 'python' 단어가 없는 게시글):")
for article in chained_query:
    print(f"- {article.title} ({article.created.strftime('%Y-%m-%d')})")