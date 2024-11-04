package com.tistory.blog.domain.entity;


import jakarta.persistence.*;
import jakarta.validation.constraints.NotEmpty;
import lombok.*;
import org.springframework.stereotype.Component;
import org.springframework.util.Assert;

@NoArgsConstructor(access = AccessLevel.PROTECTED)
//@AllArgsConstructor
@Getter
//@Builder
//@Component
@Entity
@Table(name = "account")
public class AccountEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @NotEmpty
    @Column(name = "bank_name", nullable = false)
    private String bankName;

    @NotEmpty
    @Column(name = "account_number", nullable = false)
    private String accountNumber;

    @NotEmpty
    @Column(name = "account_holder", nullable = false)
    private String accountHolder;

    // 불안전한 객채 생성 패턴
//    @Builder
//    public AccountEntity(String bankName, String accountNumber, String accountHolder) {
//        this.bankName = bankName;
//        this.accountNumber = accountNumber;
//        this.accountHolder = accountHolder;
//    }

    // 안전한 객채 생성 패턴
    @Builder
    public AccountEntity(String bankName, String accountNumber, String accountHolder) {
        Assert.hasText(bankName, "bankName must not be empty");
        Assert.hasText(accountNumber, "accountNumber must not be empty");
        Assert.hasText(accountHolder, "accountHolder must not be empty");

        this.bankName = bankName;
        this.accountNumber = accountNumber;
        this.accountHolder = accountHolder;
    }
}
