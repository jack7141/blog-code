from customers.models import Client, Domain

# 공용 테넌트 생성
tenant = Client(schema_name='public', name='Public Tenant',paid_until='2030-12-31',on_trial=False)
tenant.save()

# 공용 도메인 연결
domain = Domain()
domain.domain = 'localhost'  # 로컬 개발 환경
domain.tenant = tenant
domain.is_primary = True
domain.save()

# 추가 테넌트 생성 예시
tenant1 = Client(schema_name='tenant1',name='First Client',paid_until='2025-12-31',on_trial=True)
tenant1.save()

# 테넌트 도메인 연결
domain2 = Domain()
domain2.domain = 'tenant1.localhost'  # 로컬 개발용
domain2.tenant = tenant1
domain2.is_primary = True
domain2.save()

tenant2 = Client(schema_name='tenant2',name='Second Client',paid_until='2025-12-31',on_trial=True)
tenant2.save()

# 테넌트 도메인 연결
domain3 = Domain()
domain3.domain = 'tenant2.localhost'  # 로컬 개발용
domain3.tenant = tenant2
domain3.is_primary = True
domain3.save()