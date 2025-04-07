from django.test import TestCase
from django.contrib.auth import get_user_model

User = get_user_model()

class UserModelTest(TestCase):
    def setUp(self):
        """테스트에 필요한 데이터 설정"""
        self.user_data = {
            'username': 'testuser',
            'user_id': 'test123',
        }
        self.user = User.objects.create(**self.user_data)

    def test_create_user(self):
        """사용자 생성 테스트"""
        # 사용자가 정상적으로 생성되었는지 확인
        self.assertTrue(isinstance(self.user, User))
        self.assertEqual(self.user.username, self.user_data['username'])
        self.assertEqual(self.user.user_id, self.user_data['user_id'])
        self.assertIsNone(self.user.password)  # password가 None인지 확인

    def test_read_user(self):
        """사용자 조회 테스트"""
        # 데이터베이스에서 사용자 조회
        retrieved_user = User.objects.get(id=self.user.id)
        self.assertEqual(retrieved_user.username, self.user_data['username'])
        self.assertEqual(retrieved_user.user_id, self.user_data['user_id'])

    def test_update_user(self):
        """사용자 정보 수정 테스트"""
        # 사용자 정보 수정
        new_username = 'updateduser'
        self.user.username = new_username
        self.user.save()

        # 변경된 정보 확인
        updated_user = User.objects.get(id=self.user.id)
        self.assertEqual(updated_user.username, new_username)

    def test_delete_user(self):
        """사용자 삭제 테스트"""
        # 사용자 ID 저장
        user_id = self.user.id

        # 사용자 삭제 전 상태 확인
        self.assertTrue(User.objects.filter(id=user_id).exists())

        # 사용자 삭제
        self.user.delete()

        # 삭제 후 사용자 조회
        deleted_user = User.objects.get(id=user_id)

        # 소프트 삭제 필드 확인 (SoftDeletableModel의 구현에 따라 필드명이 달라질 수 있음)
        self.assertTrue(getattr(deleted_user, 'is_removed', False))

        # 또는 소프트 삭제가 적용된 쿼리셋 확인
        if hasattr(User, 'all_objects'):
            # 모든 객체(삭제된 객체 포함)를 조회하는 매니저가 있다면 사용
            self.assertTrue(User.all_objects.filter(id=user_id).exists())

    def test_create_user_with_password(self):
        """비밀번호가 있는 사용자 생성 테스트"""
        user_with_pwd = User.objects.create(
            username='userwithpassword',
            user_id='pwd123',
            password='securepassword'
        )
        self.assertEqual(user_with_pwd.password, 'securepassword')
