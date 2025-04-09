from users.models import User
from articles.models import Article
# python manage.py shell < queryset_demo.py

print("=== 기본 필터링 예제 ===")

all_articles = Article.objects.all()
all_users = User.objects.all()
print(all_articles.count())
print(all_users.count())