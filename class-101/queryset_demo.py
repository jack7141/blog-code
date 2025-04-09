from django.utils import timezone
import datetime

from users.models import User
from articles.models import Article, Tag
from interaction.models import Comment, Like

print("============ Django QuerySet 심화 예제 ============")

# 1. 기본 필터링과 체이닝
print("\n=== 1. 여러 조건을 체이닝한 필터링 ===")
# 여러 필터를 체이닝하여 복잡한 조건 표현
recent_published_articles = Article.objects.filter(
    is_published=True
).filter(
    created__gte=timezone.now() - datetime.timedelta(days=30)
).order_by('-created')

print(f"최근 30일 내 발행된 게시글 수: {recent_published_articles.count()}")
for article in recent_published_articles[:3]:  # 처음 3개만 출력
    print(f"- {article.title} (작성일: {article.created.strftime('%Y-%m-%d')})")

# 2. 복잡한 lookups 사용하기
print("\n=== 2. 다양한 lookup 타입 활용 ===")
# 다양한 lookup 타입 (icontains, startswith, in, range 등)
keyword_articles = Article.objects.filter(title__icontains='django')
print(f"'django'가 제목에 포함된 게시글 수: {keyword_articles.count()}")

# 특정 단어로 시작하는 게시글
starts_with_articles = Article.objects.filter(title__startswith='Django')
print(f"'Django'로 시작하는 게시글 수: {starts_with_articles.count()}")

# 여러 조건 중 하나라도 만족하는 게시글 (IN 쿼리)
specific_articles = Article.objects.filter(id__in=[1, 3, 5])
print(f"ID가 1, 3, 5인 게시글 수: {specific_articles.count()}")

# 날짜 범위 검색
one_week_ago = timezone.now() - datetime.timedelta(days=7)
two_weeks_ago = timezone.now() - datetime.timedelta(days=14)
date_range_articles = Article.objects.filter(created__range=(two_weeks_ago, one_week_ago))
print(f"1~2주 전에 작성된 게시글 수: {date_range_articles.count()}")

# 3. distinct(), values(), values_list() 활용
print("\n=== 3. distinct(), values(), values_list() 활용 ===")
# 중복 제거 (distinct)
unique_authors = Article.objects.values_list('author', flat=True).distinct()
print(f"글을 작성한 고유 사용자 수: {len(unique_authors)}")

# values()로 딕셔너리 형태로 가져오기
article_dicts = Article.objects.values('id', 'title', 'author__username')[:3]
print("values() 결과 (딕셔너리 형태):")
for article in article_dicts:
    print(f"- {article}")

# values_list()로 튜플 형태로 가져오기
article_tuples = Article.objects.values_list('id', 'title')[:3]
print("values_list() 결과 (튜플 형태):")
for article in article_tuples:
    print(f"- {article}")

# 4. exclude() - 특정 조건을 제외한 결과 가져오기
print("\n=== 4. exclude() 활용 ===")
# 특정 조건을 제외
unpublished_articles = Article.objects.exclude(is_published=True)
print(f"발행되지 않은 게시글 수: {unpublished_articles.count()}")

# 여러 조건 제외하기
filtered_articles = Article.objects.exclude(
    title__icontains='django'
).exclude(
    author__username='admin'
)
print(f"제목에 'django'가 없고, admin이 작성하지 않은 게시글 수: {filtered_articles.count()}")


# 6. order_by() - 정렬하기
print("\n=== 6. order_by() 활용 ===")
# 단순 정렬
recent_articles = Article.objects.order_by('-created')[:3]
print("최근 작성된 게시글 (created 기준 내림차순):")
for article in recent_articles:
    print(f"- {article.title} ({article.created.strftime('%Y-%m-%d')})")

# 다중 필드 정렬
sorted_articles = Article.objects.order_by('author__username', '-created')[:5]
print("\n작성자 이름 오름차순, 작성일 내림차순 정렬:")
for article in sorted_articles:
    print(f"- {article.title} (작성자: {article.author.username}, 날짜: {article.created.strftime('%Y-%m-%d')})")

# 7. 조회 조합하기 - 복잡한 QuerySet 구성
print("\n=== 7. 여러 QuerySet 메서드 조합하기 ===")
# 여러 메서드 조합
complex_query = Article.objects.filter(
    is_published=True
).exclude(
    title__icontains='python'
).select_related(
    'author'
).prefetch_related(
    'tags'
).order_by(
    '-created'
)[:3]

print("복잡한 조합 쿼리 결과:")
for article in complex_query:
    tag_names = ", ".join([tag.name for tag in article.tags.all()])
    print(f"- {article.title} (작성자: {article.author.username}, 태그: {tag_names})")

# 8. exists()와 count() - 효율적인 존재 여부/개수 확인
print("\n=== 8. exists()와 count() 활용 ===")
# exists() - 결과 존재 여부만 확인 (전체 로드 없이 빠르게 확인)
has_django_articles = Article.objects.filter(title__icontains='django').exists()
print(f"Django 관련 게시글 존재 여부: {has_django_articles}")

# count() - 개수만 확인 (전체 로드 없이 빠르게 카운트)
comment_count = Comment.objects.count()
print(f"전체 댓글 수: {comment_count}")

# 9. first(), last() - 처음/마지막 레코드 가져오기
print("\n=== 9. first(), last() 활용 ===")
# first() - 첫 번째 레코드 가져오기
newest_article = Article.objects.order_by('-created').first()
if newest_article:
    print(f"가장 최근 게시글: {newest_article.title} ({newest_article.created.strftime('%Y-%m-%d')})")

# last() - 마지막 레코드 가져오기
oldest_article = Article.objects.order_by('-created').last()
if oldest_article:
    print(f"가장 오래된 게시글: {oldest_article.title} ({oldest_article.created.strftime('%Y-%m-%d')})")

# 10. get_or_create() 와 update_or_create() - 없으면 생성하기
print("\n=== 10. get_or_create()와 update_or_create() 활용 ===")
# get_or_create() - 존재하면 가져오고, 없으면 생성
tag, created = Tag.objects.get_or_create(name='Django ORM')
print(f"태그 '{tag.name}' {' 생성됨' if created else ' 이미 존재함'}")

# 11. none() - 빈 QuerySet 생성
print("\n=== 11. none() 활용 ===")
empty_queryset = Article.objects.none()
print(f"빈 QuerySet 길이: {len(empty_queryset)}")

# 12. using() - 다중 데이터베이스 사용 시
print("\n=== 12. using() 활용 (다중 DB) ===")
# using() 메서드는 다중 데이터베이스 환경에서 특정 DB 지정
# 예제에서는 실제로 실행되지 않고 문법만 보여줌
print("# 특정 데이터베이스 사용 예시 (실행되지 않음)")
print("Article.objects.using('replica').all()")

print("\n========== QuerySet 심화 예제 종료 ==========")