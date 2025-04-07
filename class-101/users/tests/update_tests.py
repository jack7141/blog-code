from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTest(TestCase):
    def test_update_user(self):
        """사용자 정보 수정 테스트"""
        # 사용자 정보 수정
        new_username = 'updateduser'
        self.user.username = new_username
        self.user.save()

        # 변경된 정보 확인
        updated_user = User.objects.get(id=self.user.id)
        self.assertEqual(updated_user.username, new_username)