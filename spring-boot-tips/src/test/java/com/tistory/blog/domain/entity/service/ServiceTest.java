package com.tistory.blog.domain.entity.service;

import com.tistory.blog.domain.entity.AccountEntity;
import org.junit.jupiter.api.Test;

public class ServiceTest {
    @Test
    void TestNoArgsConstructor() {
        /*@NoArgsConstructor(access = AccessLevel.PROTECTED)
         * 어노테이션을 사용했을 경우 다른 패키지에서 인스턴스를 선언하면,
         *  reason: AccountEntity() has protected access in AccountEntity
         */
        AccountEntity accountEntity = new AccountEntity();
        System.out.println("AccountEntity 객체: " + accountEntity.toString());
    }
}
