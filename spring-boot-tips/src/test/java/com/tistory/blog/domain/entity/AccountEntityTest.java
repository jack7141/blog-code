package com.tistory.blog.domain.entity;

import org.junit.jupiter.api.DisplayName;
import org.junit.jupiter.api.Test;

import static org.assertj.core.api.AssertionsForClassTypes.assertThat;
import static org.junit.jupiter.api.Assertions.*;

class AccountEntityTest {

    String BANKNAME = "우리은행";
    String ACCOUNTNUMBER = "123-123-123-123";
    String ACCOUNTHOLDER = "ME";

    @Test
    @DisplayName(value = "불안전한 객채 생성 패턴")
    void createUnstableAccountEntity() {
        AccountEntity accountEntity = AccountEntity.builder()
                .accountHolder("")
                .accountNumber(ACCOUNTNUMBER)
                .bankName(BANKNAME)
                .build();
        assertThat(accountEntity.getBankName()).isEqualTo(BANKNAME);
        assertThat(accountEntity.getAccountNumber()).isEqualTo(ACCOUNTNUMBER);
        System.out.println("AccountEntity 객체 : " + accountEntity.toString());
    }

    @Test
    @DisplayName(value = "안정적인 객채 생성 패턴")
    void createstableAccountEntity() {
        AccountEntity accountEntity = AccountEntity.builder()
                .accountHolder("")
                .accountNumber(ACCOUNTNUMBER)
                .bankName(BANKNAME)
                .build();
        assertThat(accountEntity.getBankName()).isEqualTo(BANKNAME);
        assertThat(accountEntity.getAccountNumber()).isEqualTo(ACCOUNTNUMBER);
        System.out.println("AccountEntity 객체 : " + accountEntity.toString());
    }

    @Test
    @DisplayName(value = "안정적인 객채 생성 빌더 이름 명명 + builderClassName 생략")
    void createAccountEntityBuilderName() {
        AccountEntity accountEntity = AccountEntity.creditAccountBuilder()
                .accountHolder("")
                .accountNumber(ACCOUNTNUMBER)
                .bankName(BANKNAME)
                .build();
        assertThat(accountEntity.getBankName()).isEqualTo(BANKNAME);
        assertThat(accountEntity.getAccountNumber()).isEqualTo(ACCOUNTNUMBER);
        System.out.println("AccountEntity 객체 : " + accountEntity.toString());
    }
}