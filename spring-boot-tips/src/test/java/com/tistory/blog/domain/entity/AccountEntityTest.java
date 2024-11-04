package com.tistory.blog.domain.entity;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.junit.jupiter.api.Assertions.*;

class AccountEntityTest {
    @Test
    @DisplayName(value = "안전한 객채 생성 패턴")
    void createAccountEntity() {
        AccountEntity accountEntity = AccountEntity.builder().build();
    }

}