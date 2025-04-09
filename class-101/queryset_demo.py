from django.db.models import Count, Q, F
from django.db.models.aggregates import Avg, Max
from django.utils import timezone
import datetime

from users.models import User
from articles.models import Article
# python manage.py shell < queryset_demo.py

print("=== 기본 필터링 예제 ===")

print("=== 기본 필터링 예제 ===")
# 기본 필터링
all_articles = Article.objects.all()
print(f"총 게시글 수: {all_articles.count()}")

django_articles = Article.objects.filter(title__icontains='django')
print(f"Django 관련 게시글 수: {django_articles.count()}")

# 날짜 필터링
one_week_ago = timezone.now() - datetime.timedelta(days=7)
recent_articles = Article.objects.filter(created__gte=one_week_ago)
print(f"최근 일주일 게시글 수: {recent_articles.count()}")

print("\n=== Q 객체를 활용한 복잡한 조건 ===")
# Q 객체 활용
complex_query = Article.objects.filter(
    Q(title__icontains='django') | Q(content__icontains='python')
)
print(f"Django 또는 Python 관련 게시글 수: {complex_query.count()}")

# 더 복잡한 조건
advanced_query = Article.objects.filter(
    (Q(title__icontains='django') & Q(created__gte=one_week_ago))
)
print(f"최근 Django 게시글 또는 관리자 게시글 수: {advanced_query.count()}")

print("\n=== 주석(annotate)과 집계(aggregate) ===")
# 게시글별 댓글 수 계산
articles_with_comments = Article.objects.annotate(comment_count=Count('comments'))
for article in articles_with_comments[:3]:  # 처음 3개만 출력
    print(f"제목: {article.title}, 댓글 수: {article.comment_count}")

# 전체 통계
# stats = Article.objects.aggregate(
#     total_count=Count('id'),
#     avg_comments=Avg('comments'),
#     max_created=Max('created')
# )
# print(f"통계: {stats}")
