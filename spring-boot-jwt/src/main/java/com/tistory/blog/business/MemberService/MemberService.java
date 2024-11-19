package com.tistory.blog.business.MemberService;

import com.tistory.blog.core.exception.DuplicateMemberException;
import com.tistory.blog.domain.dto.member.MemberDTO;
import com.tistory.blog.domain.dto.Request.SignupDTO;
import com.tistory.blog.domain.entity.MemberEntity;
import com.tistory.blog.domain.entity.RoleEntity;
import com.tistory.blog.persistence.MemberRepository.MemberRepository;
import com.tistory.blog.persistence.RoleRepository.RoleRepository;
import jakarta.transaction.Transactional;
import lombok.RequiredArgsConstructor;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
@Transactional
@RequiredArgsConstructor
public class MemberService {

    private final MemberRepository memberRepository;
    private final RoleRepository roleRepository;
    private final BCryptPasswordEncoder encoder;

    public MemberDTO Signup(SignupDTO signupDTO) {
        /*
        * 회원가입시 Email, 핸드폰번호 중복 유효성 검사
        * */
        ValidateDuplicateEmailAndPhone(signupDTO);

        RoleEntity roleEntity = roleRepository.findByName(signupDTO.getRole());

        MemberEntity newMember = MemberEntity.builder()
                .email(signupDTO.getEmail())
                .phone(signupDTO.getPhone())
                .username(signupDTO.getUsername())
                .role(roleEntity)
                .password(encoder.encode(signupDTO.getPassword()))
                .build();
        MemberEntity savedMember = memberRepository.save(newMember);
        return MemberDTO.of(savedMember);
    }

    void ValidateDuplicateEmailAndPhone(SignupDTO signupDTO){
        if (memberRepository.existsByEmailOrPhone(signupDTO.getEmail(), signupDTO.getPhone())) {
            throw new DuplicateMemberException("중복된 이메일 또는 핸드폰 번호로 회원 가입을 시도했습니다.");
        }
    }
}
