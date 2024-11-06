package com.tistory.blog.domain.dto.member;

import com.tistory.blog.domain.entity.MemberEntity;
import jakarta.validation.constraints.Email;
import jakarta.validation.constraints.NotBlank;
import lombok.Builder;
import lombok.Data;

@Data
@Builder
public class MemberDTO {
    @NotBlank(message = "이메일을 입력해주세요.")
    @Email(message = "이메일 형식으로 입력해주세요.")
    private String email;

    @NotBlank(message = "비밀번호를 입력해주세요.")
    private String password;

    @NotBlank(message = "이름을 입력해주세요.")
    private String username;

    @NotBlank(message = "핸드폰 번호를 입력해주세요.")
    private String phone;

    public static MemberDTO of(MemberEntity member) {
        return MemberDTO.builder()
                .username(member.getUsername())
                .email(member.getEmail())
                .phone(member.getPhone())
                .build();
    }
}
