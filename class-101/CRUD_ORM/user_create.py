from users.models import User

new_user = User(
    username='홍길동',
    user_id='new123'
)
new_user.save()
print(f"새 사용자 생성됨: {new_user.username}, ID: {new_user.id}")

# 방법 2: create() 메서드 사용
quick_user = User.objects.create(
    username='newuser',
    user_id='quick456'
)
print(f"create()로 생성된 사용자: {quick_user.username}, ID: {quick_user.id}")