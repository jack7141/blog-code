package com.tistory.blog.domain.entity;

import jakarta.persistence.*;
import jakarta.validation.constraints.NotEmpty;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.util.Assert;

@NoArgsConstructor(access = lombok.AccessLevel.PROTECTED)
@Data
@Entity
@Table(name = "member")
public class MemberEntity {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "id")
    private Long id;

    @Column(name = "username")
    private String username;

    @NotEmpty
    @Column(name = "password")
    private String password;

    @NotEmpty
    @Column(name = "phone", nullable = false, unique = true)
    private String phone;

    @NotEmpty
    @Column(name = "email", nullable = false, unique = true)
    private String email;

    @Builder
    public MemberEntity(String username, String password, String phone, String email) {
        Assert.hasText(username, "username 값이 누락되었습니다.");
        Assert.hasText(password, "password 값이 누락되었습니다.");
        Assert.hasText(phone, "phone 값이 누락되었습니다.");
        Assert.hasText(email, "email 값이 누락되었습니다.");

        this.username = username;
        this.password = password;
        this.phone = phone;
        this.email = email;
    }

    @Override
    public String toString() {
        return String.format("MemberEntity[id=%d, username='%s', phone='%s', email='%s']",
                id, username, phone, email);
    }
}
