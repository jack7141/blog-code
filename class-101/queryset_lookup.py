# 다양한 lookup 타입 활용
# 대소문자 구분 없이 포함된 문자열 검색 (icontains)
import datetime

from django.utils import timezone

from articles.models import Article

# 대소문자 구분 없이 포함된 문자열 검색 (icontains)
django_articles = Article.objects.filter(title__icontains='django')
print(f"'django'가 제목에 포함된 게시글 수: {django_articles.count()}")

# 특정 문자열로 시작하는 항목 찾기 (startswith)
python_articles = Article.objects.filter(title__startswith='Python')
print(f"'Python'으로 시작하는 게시글 수: {python_articles.count()}")

# 특정 문자열로 끝나는 항목 찾기 (endswith)
guide_articles = Article.objects.filter(title__endswith='가이드')
print(f"'가이드'로 끝나는 게시글 수: {guide_articles.count()}")

# 특정 값들 중 하나와 일치하는 항목 찾기 (in)
specific_articles = Article.objects.filter(id__in=[1, 3, 5])
print(f"ID가 1, 3, 5 중 하나인 게시글 수: {specific_articles.count()}")

# 범위 검색 (range)
one_week_ago = timezone.now() - datetime.timedelta(days=7)
one_month_ago = timezone.now() - datetime.timedelta(days=30)
recent_articles = Article.objects.filter(created__range=(one_month_ago, one_week_ago))
print(f"1주일~1달 사이에 작성된 게시글 수: {recent_articles.count()}")

# 특정 날짜보다 이후에 생성된 게시글 (gt: greater than)
newer_articles = Article.objects.filter(created__gt=one_week_ago)
print(f"일주일 이내 작성된 게시글 수: {newer_articles.count()}")

# 특정 날짜보다 이전에 생성된 게시글 (lt: less than)
older_articles = Article.objects.filter(created__lt=one_month_ago)
print(f"한달보다 오래된 게시글 수: {older_articles.count()}")