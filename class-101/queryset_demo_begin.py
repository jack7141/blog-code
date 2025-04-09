from django.utils import timezone
import datetime

from users.models import User
from articles.models import Article, Tag
from interaction.models import Comment, Like

print("============ Django QuerySet 기본/중급 활용 예제 ============")

# 1. 기본 필터링
print("\n=== 1. 기본 필터링 ===")

# 모든 게시글 조회
all_articles = Article.objects.all()
print(f"총 게시글 수: {all_articles.count()}")

# 조건으로 필터링
published_articles = Article.objects.filter(is_published=True)
print(f"발행된 게시글 수: {published_articles.count()}")

# 특정 ID로 단일 객체 가져오기
try:
    first_article = Article.objects.get(id=1)
    print(f"ID가 1인 게시글 제목: {first_article.title}")
except Article.DoesNotExist:
    print("ID가 1인 게시글이 없습니다.")

# 2. 다양한 lookup 타입 활용
print("\n=== 2. 다양한 lookup 타입 활용 ===")

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

# 3. 정렬 (order_by)
print("\n=== 3. 정렬 (order_by) ===")

# 최신순 정렬
recent_articles = Article.objects.order_by('-created')[:3]
print("최근에 작성된 게시글 (최신순):")
for article in recent_articles:
    print(f"- {article.title} ({article.created.strftime('%Y-%m-%d')})")

# 오래된순 정렬
oldest_articles = Article.objects.order_by('created')[:3]
print("\n가장 오래된 게시글:")
for article in oldest_articles:
    print(f"- {article.title} ({article.created.strftime('%Y-%m-%d')})")

# 제목 알파벳순 정렬
title_sorted = Article.objects.order_by('title')[:3]
print("\n제목 알파벳순 정렬:")
for article in title_sorted:
    print(f"- {article.title}")

# 여러 필드로 정렬 (작성자 이름순, 같은 작성자면 최신순)
author_date_sorted = Article.objects.order_by('author__username', '-created')[:5]
print("\n작성자 이름순, 같은 작성자면 최신순:")
for article in author_date_sorted:
    print(f"- {article.title} (작성자: {article.author.username}, 날짜: {article.created.strftime('%Y-%m-%d')})")

# 4. 조건 제외하기 (exclude)
print("\n=== 4. 조건 제외하기 (exclude) ===")

# 미발행 게시글 찾기
unpublished = Article.objects.exclude(is_published=True)
print(f"발행되지 않은 게시글 수: {unpublished.count()}")

# 특정 단어가 제목에 포함되지 않는 게시글
non_django = Article.objects.exclude(title__icontains='django')
print(f"제목에 'django'가 포함되지 않은 게시글 수: {non_django.count()}")

# 특정 작성자의 게시글 제외
non_admin = Article.objects.exclude(author__username='admin')
print(f"admin이 작성하지 않은 게시글 수: {non_admin.count()}")

# 5. 중복 제거 (distinct)
print("\n=== 5. 중복 제거 (distinct) ===")

# 게시글을 작성한 고유 사용자 ID 목록
author_ids = Article.objects.values_list('author', flat=True).distinct()
print(f"게시글을 작성한 고유 사용자 수: {len(author_ids)}")

# 6. values와 values_list - 필요한 필드만 가져오기
print("\n=== 6. values와 values_list ===")

# values() - 딕셔너리 형태로 반환
articles_dict = Article.objects.values('id', 'title', 'author__username')[:3]
print("딕셔너리 형태로 받기 (values):")
for item in articles_dict:
    print(f"- ID: {item['id']}, 제목: {item['title']}, 작성자: {item.get('author__username', 'Unknown')}")

# values_list() - 튜플 형태로 반환
articles_tuple = Article.objects.values_list('id', 'title')[:3]
print("\n튜플 형태로 받기 (values_list):")
for item in articles_tuple:
    print(f"- ID: {item[0]}, 제목: {item[1]}")

# flat=True 옵션으로 단일 필드만 리스트로 받기
article_titles = Article.objects.values_list('title', flat=True)[:5]
print("\n제목만 리스트로 받기 (flat=True):")
for title in article_titles:
    print(f"- {title}")

# 7. 체이닝 - 여러 메서드 연결하기
print("\n=== 7. 체이닝 - 여러 메서드 연결하기 ===")

# 여러 조건을 차례로 적용
chained_query = Article.objects.filter(is_published=True).filter(created__gte=one_week_ago).exclude(title__icontains='python').order_by('-created')[:3]

print("체이닝 결과 (최근 1주일 내 발행된, 'python' 단어가 없는 게시글):")
for article in chained_query:
    print(f"- {article.title} ({article.created.strftime('%Y-%m-%d')})")

# 8. 유용한 단일 항목 조회 메서드
print("\n=== 8. 유용한 단일 항목 조회 메서드 ===")

# first() - 첫 번째 항목 가져오기
first_published = Article.objects.filter(is_published=True).order_by('-created').first()
if first_published:
    print(f"가장 최근에 발행된 게시글: {first_published.title}")

# last() - 마지막 항목 가져오기
last_published = Article.objects.filter(is_published=True).order_by('-created').last()
if last_published:
    print(f"가장 오래전에 발행된 게시글: {last_published.title}")

# 9. exists(), count() - 존재 여부와 개수 확인
print("\n=== 9. exists(), count() - 존재 여부와 개수 확인 ===")

# exists() - 결과가 존재하는지 불리언으로 반환
has_python_articles = Article.objects.filter(title__icontains='python').exists()
print(f"Python 관련 게시글 존재 여부: {has_python_articles}")

# count() - 개수 반환
total_comments = Comment.objects.count()
print(f"총 댓글 수: {total_comments}")

# 10. get_or_create, update_or_create - 없으면 생성하기
print("\n=== 10. get_or_create, update_or_create ===")

# get_or_create() - 있으면 가져오고, 없으면 생성
tag, created = Tag.objects.get_or_create(name='FastAPI')
print(f"태그 '{tag.name}'는 {'새로 생성됨' if created else '이미 존재함'}")

# 11. none() - 빈 QuerySet 생성
print("\n=== 11. none() - 빈 QuerySet 생성 ===")
empty_queryset = Article.objects.none()
print(f"빈 QuerySet의 개수: {empty_queryset.count()}")

# 12. slice - 특정 범위만 가져오기
print("\n=== 12. slice - 특정 범위만 가져오기 ===")
# slice를 통한 페이지네이션
page_articles = Article.objects.all()[5:10]  # 6번째부터 10번째까지
print(f"6~10번째 게시글 목록:")
for article in page_articles:
    print(f"- {article.title}")

# 13. only(), defer() - 특정 필드만 가져오거나 제외하기
print("\n=== 13. only(), defer() - 특정 필드 최적화 ===")

# only() - 특정 필드만 가져오기
articles_only_title = Article.objects.only('title')[:3]
print("제목만 가져오기 (only):")
for article in articles_only_title:
    print(vars(article))
    print(f"- {article.title}")

# defer() - 특정 필드 제외하고 가져오기
articles_defer_content = Article.objects.defer('content')[:3]
print("\n내용 제외하고 가져오기 (defer):")
for article in articles_defer_content:
    print(f"- {article.title} (ID: {article.id})")

print("\n=========== QuerySet 예제 종료 ===========")