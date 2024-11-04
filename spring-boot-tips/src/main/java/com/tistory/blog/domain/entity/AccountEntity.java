package com.tistory.blog.domain.entity;


import jakarta.persistence.*;
import jakarta.validation.constraints.NotEmpty;
import lombok.*;
import org.springframework.stereotype.Component;
import org.springframework.util.Assert;

//@AllArgsConstructor
//@Builder
//@Component
@Entity
@Table(name = "account")
@NoArgsConstructor(access = AccessLevel.PROTECTED)
@Getter
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
//    @Builder
//    public AccountEntity(String bankName, String accountNumber, String accountHolder) {
//        Assert.hasText(bankName, "bankName 값이 누락되었습니다.");
//        Assert.hasText(accountNumber, "accountNumber 값이 누락되었습니다.");
//        Assert.hasText(accountHolder, "accountHolder 값이 누락되었습니다.");
//
//        this.bankName = bankName;
//        this.accountNumber = accountNumber;
//        this.accountHolder = accountHolder;
//    }

    // 안전한 객채 생성 이름 부여
    @Builder(builderClassName = "CreditAccountBuilder", builderMethodName = "creditAccountBuilder")
    public AccountEntity(String bankName, String accountNumber, String accountHolder) {
        Assert.hasText(bankName, "bankName 값이 누락되었습니다.");
        Assert.hasText(accountNumber, "accountNumber 값이 누락되었습니다.");
        Assert.hasText(accountHolder, "accountHolder 값이 누락되었습니다.");

        this.bankName = bankName;
        this.accountNumber = accountNumber;
        this.accountHolder = accountHolder;
    }

    @Override
    public String toString() {
        return "AccountEntity{" +
                "id=" + id +
                ", bankName='" + bankName + '\'' +
                ", accountNumber='" + accountNumber + '\'' +
                ", accountHolder='" + accountHolder + '\'' +
                '}';
    }
}
