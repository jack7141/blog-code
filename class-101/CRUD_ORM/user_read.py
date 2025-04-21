from users.models import User


# 전체 사용자 조회
all_users = User.objects.all()
print(f"총 사용자 수: {all_users.count()}")
print("사용자 목록:")
for user in all_users[:5]:  # 처음 5명만 출력
    print(f" - {user.username} (ID: {user.id}, 유저ID: {user.user_id})")

# 특정 사용자 조회 (get)
try:
    user = User.objects.get(username='newuser')
    print(f"\nget()으로 조회: {user.username}, ID: {user.id}")
except User.DoesNotExist:
    print("\n해당 사용자가 존재하지 않습니다.")

# 조건에 맞는 사용자 조회 (filter)
filtered_users = User.objects.filter(username='newuser')
print(f"\n'new'로 시작하는 사용자 수: {filtered_users.count()}")

