# 방법 1: 객체 조회 후 수정 및 저장
from users.models import User

try:
    user = User.objects.get(username='newuser')
    print(f"수정 전: {user.username}, 유저ID: {user.user_id}")

    # 필드 값 수정
    user.username = 'updateduser'
    user.user_id = 'updated123'
    user.save()

    # 다시 조회하여 변경 확인
    updated_user = User.objects.get(id=user.id)
    print(f"수정 후: {updated_user.username}, 유저ID: {updated_user.user_id}")

except User.DoesNotExist:
    print("해당 사용자가 존재하지 않습니다.")


# 방법 2: update() 메서드로 일괄 수정
updated_count = User.objects.filter(
    username='홍길동'
).update(user_id='bulk_updated789')

print(f"\nupdate() 메서드로 {updated_count}명의 사용자 정보 업데이트됨")

# 수정된 결과 확인
updated_users = User.objects.filter(user_id='bulk_updated789')
for user in updated_users:
    print(f" - {user.username}, 유저ID: {user.user_id}")