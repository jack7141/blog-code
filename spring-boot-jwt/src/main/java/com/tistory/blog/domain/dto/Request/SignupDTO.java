package com.tistory.blog.domain.dto.Request;

import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import lombok.Builder;
import lombok.Data;

@Data
public class SignupDTO {
    @NotBlank(message = "이메일을 입력해주세요.")
    @Email(message = "유효한 이메일 주소를 입력해주세요.", regexp = "^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}$")
    private String email;

    @NotBlank(message = "비밀번호를 입력해주세요.")
    private String password;

    @NotBlank(message = "이름을 입력해주세요.")
    private String username;

    @NotBlank(message = "핸드폰 번호를 입력해주세요.")
    private String phone;

    private String role;

    @Builder
    public SignupDTO(String email, String password, String username, String phone, String role) {
        this.email = email;
        this.password = password;
        this.username = username;
        this.phone = phone;
        this.role = (role == null || role.isEmpty()) ? "USER" : role;
    }
}
