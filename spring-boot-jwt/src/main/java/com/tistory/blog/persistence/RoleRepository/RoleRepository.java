package com.tistory.blog.persistence.RoleRepository;

import com.tistory.blog.domain.entity.MemberEntity;
import com.tistory.blog.domain.entity.RoleEntity;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;

import java.util.Optional;

@Repository
public interface RoleRepository extends JpaRepository<RoleEntity, Long> {
    RoleEntity findByName(String name);
}
