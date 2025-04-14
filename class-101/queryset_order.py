# queryset_order.py
from articles.models import Article

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
