# create_test_data.py

from django.utils import timezone
from django.contrib.contenttypes.models import ContentType
import random
import string
from datetime import timedelta

from users.models import User
from articles.models import Article, Tag
from interaction.models import Comment, Like

# 데이터 삭제 (필요시 주석 해제)
# User.objects.all().delete()
# Article.objects.all().delete()
# Comment.objects.all().delete()
# Like.objects.all().delete()
# Tag.objects.all().delete()

print("==== 테스트 데이터 생성 시작 ====")


# 랜덤 문자열 생성 헬퍼 함수
def random_string(length=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


# 사용자 생성
users = []
usernames = ["admin", "testuser", "django_lover", "python_dev", "web_designer"]
user_ids = ["admin123", "test123", "django123", "python123", "web123"]

for i in range(5):
    username = usernames[i]
    user_id = user_ids[i]

    user, created = User.objects.get_or_create(
        username=username,
        defaults={
            'user_id': user_id,
            'is_active': True
        }
    )

    if created:
        user.set_password('password123')
        user.save()
        print(f"사용자 생성: {username}")
    else:
        print(f"기존 사용자 사용: {username}")

    users.append(user)

# 태그 생성
tags = []
tag_names = ["Django", "Python", "ORM", "Web", "Backend", "Frontend", "Database", "Tutorial"]

for tag_name in tag_names:
    tag, created = Tag.objects.get_or_create(name=tag_name)
    if created:
        print(f"태그 생성: {tag_name}")
    else:
        print(f"기존 태그 사용: {tag_name}")
    tags.append(tag)

# 게시글 생성
articles = []
titles = [
    "Django 튜토리얼 - 시작하기",
    "Django ORM 완벽 가이드",
    "Python으로 웹 개발하기",
    "Django 모델 관계 설계 방법",
    "Django로 블로그 만들기",
    "Django 템플릿 시스템 이해하기",
    "Django REST framework 사용법",
    "Django 테스트 작성하기",
    "Python과 SQLAlchemy vs Django ORM",
    "Django 배포 가이드",
    "Django Admin 커스터마이징",
    "Django에서 이미지 처리하기",
    "Django 인증 시스템 구현",
    "Django와 Ajax 통합하기",
    "Python 웹 프레임워크 비교"
]

contents = [
    "Django는 Python으로 작성된 오픈 소스 웹 프레임워크로, 빠르고 깔끔한 개발을 장려합니다.",
    "Django ORM은 객체-관계 매핑 도구로, SQL 쿼리를 Python 코드로 작성할 수 있게 해줍니다.",
    "Python은 웹 개발에 매우 적합한 언어로, Django와 같은 프레임워크를 통해 쉽게 웹 애플리케이션을 구축할 수 있습니다.",
    "Django에서는 일대다, 다대다, 일대일 등 다양한 모델 관계를 쉽게 설정할 수 있습니다.",
    "Django로 블로그를 만드는 과정을 단계별로 설명합니다. 모델 설계부터 뷰 작성, 템플릿 구성까지 모든 과정을 다룹니다.",
    "Django의 템플릿 시스템은 HTML 페이지 생성을 위한 강력한 도구입니다. 변수, 필터, 태그 등을 활용하는 방법을 알아봅니다.",
    "Django REST framework는 API 개발을 위한 강력한 도구로, 인증, 권한, 스로틀링 등 다양한 기능을 제공합니다.",
    "Django에서 테스트 작성은 중요합니다. 단위 테스트와 통합 테스트를 작성하는 방법을 설명합니다.",
    "Python ORM 도구인 SQLAlchemy와 Django ORM의 차이점과 각각의 장단점을 비교합니다.",
    "Django 애플리케이션을 프로덕션 환경에 배포하는 방법과 최적화 방법을 설명합니다.",
    "Django Admin 인터페이스를 커스터마이징하여 관리자 경험을 향상시키는 방법을 알아봅니다.",
    "Django에서 이미지 업로드, 크기 조정, 처리 등을 구현하는 방법을 설명합니다.",
    "Django의 인증 시스템을 활용하여 로그인, 회원가입, 비밀번호 재설정 등의 기능을 구현하는 방법을 알아봅니다.",
    "Django와 Ajax를 통합하여 동적 웹 페이지를 구현하는 방법을 설명합니다.",
    "Django, Flask, FastAPI 등 다양한 Python 웹 프레임워크의 특징과 장단점을 비교합니다."
]

# 게시글 생성 (최근 30일 범위 내에서 랜덤 날짜로)
now = timezone.now()
for i in range(15):
    # 랜덤 날짜 생성 (최근 30일 이내)
    random_days = random.randint(0, 30)
    random_hours = random.randint(0, 23)
    random_minutes = random.randint(0, 59)
    created_date = now - timedelta(days=random_days, hours=random_hours, minutes=random_minutes)

    # 랜덤 작성자 선택
    author = random.choice(users)

    # 게시글 생성
    article, created = Article.objects.get_or_create(
        title=titles[i],
        defaults={
            'content': contents[i],
            'author': author,
            'created': created_date,
            'is_published': True
        }
    )

    if created:
        # 랜덤 태그 할당 (1~3개)
        tag_count = random.randint(1, 3)
        selected_tags = random.sample(tags, tag_count)
        article.tags.set(selected_tags)

        print(f"게시글 생성: {article.title} (작성자: {author.username}, 날짜: {created_date.strftime('%Y-%m-%d')})")
    else:
        print(f"기존 게시글 사용: {article.title}")

    articles.append(article)

# 게시글 ContentType 가져오기
article_content_type = ContentType.objects.get_for_model(Article)

# 댓글 생성
comments_text = [
    "좋은 글 감사합니다!",
    "정말 유익한 내용이네요.",
    "도움이 많이 되었습니다.",
    "잘 읽었습니다. 다음 글도 기대할게요.",
    "이해하기 쉽게 설명해주셔서 감사합니다.",
    "질문이 있는데요, 좀 더 자세히 설명해주실 수 있나요?",
    "예제 코드가 매우 유용했습니다.",
    "이 부분에 대해 좀 더 알고 싶습니다.",
    "실제 프로젝트에 적용해봐야겠네요.",
    "다른 관점도 고려해보면 좋을 것 같아요."
]

# 각 게시글마다 0~5개의 댓글 생성
all_comments = []
for article in articles:
    # 랜덤 댓글 수 결정 (0~5)
    comment_count = random.randint(0, 5)

    for _ in range(comment_count):
        # 랜덤 사용자와 댓글 내용 선택
        user = random.choice(users)
        text = random.choice(comments_text)

        # 랜덤 날짜 생성 (게시글 작성일 이후)
        article_date = article.created
        max_days_after = (now - article_date).days
        if max_days_after > 0:
            days_after = random.randint(0, max_days_after)
        else:
            days_after = 0
        comment_date = article_date + timedelta(days=days_after)

        # Generic Foreign Key를 사용한 댓글 생성
        comment = Comment.objects.create(
            content_type=article_content_type,
            object_id=article.id,
            user=user,
            content=text
        )

        print(f"댓글 생성: 게시글 '{article.title}'에 '{user.username}'의 댓글")
        all_comments.append(comment)

# 댓글에 대한 대댓글 생성 (20% 확률로)
comment_content_type = ContentType.objects.get_for_model(Comment)
for comment in all_comments:
    if random.random() < 0.2:  # 20% 확률로 수정
        # 랜덤 사용자와 댓글 내용 선택
        user = random.choice(users)
        text = random.choice(["동의합니다!", "좋은 의견이네요.", "감사합니다.", "말씀 감사합니다."])

        # 대댓글 생성
        reply = Comment.objects.create(
            content_type=comment_content_type,
            object_id=comment.id,
            user=user,
            content=text
        )
        print(f"대댓글 생성: '{user.username}'의 대댓글")

# 좋아요 생성 (30% 확률로)
for article in articles:
    for user in users:
        if random.random() < 0.3:  # 30% 확률로 수정
            like, created = Like.objects.get_or_create(
                content_type=article_content_type,
                object_id=article.id,
                user=user
            )
            print(f"좋아요 생성: '{user.username}'이 게시글 '{article.title}'에 좋아요 (새로 생성: {created})")

# 댓글 좋아요 생성 (10% 확률로)
for comment in all_comments:
    for user in users:
        if random.random() < 0.1:  # 10% 확률로 수정
            like, created = Like.objects.get_or_create(
                content_type=comment_content_type,
                object_id=comment.id,
                user=user
            )
            print(f"좋아요 생성: '{user.username}'이 댓글에 좋아요 (새로 생성: {created})")

print("==== 테스트 데이터 생성 완료 ====")
print(f"생성된 사용자: {User.objects.count()}명")
print(f"생성된 게시글: {Article.objects.count()}개")
print(f"생성된 댓글: {Comment.objects.count()}개")
print(f"생성된 좋아요: {Like.objects.count()}개")
print(f"생성된 태그: {Tag.objects.count()}개")