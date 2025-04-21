# 삭제 전 사용자 수 확인
from users.models import User

pre_delete_count = User.objects.count()
print(f"삭제 전 사용자 수: {pre_delete_count}")

# 방법 1: 개별 객체 삭제
try:
    user = User.objects.get(username='updateduser')
    user_id = user.id
    username = user.username
    user.delete()
    print(f"사용자 '{username}' (ID: {user_id}) 삭제됨")
except User.DoesNotExist:
    print("해당 사용자가 존재하지 않습니다.")

# 방법 2: 여러 객체 한 번에 삭제
result = User.objects.filter(username__startswith='quick').delete()
print(f"\n삭제 결과: {result}")

# 삭제 후 전체 사용자 수 확인
post_delete_count = User.objects.count()
print(f"삭제 후 사용자 수: {post_delete_count}")
print(f"삭제된 사용자 수: {pre_delete_count - post_delete_count}")

# 최종 사용자 목록 출력
print("\n최종 사용자 목록:")
for user in User.objects.all():
    print(f" - {user.username} (ID: {user.id})")
