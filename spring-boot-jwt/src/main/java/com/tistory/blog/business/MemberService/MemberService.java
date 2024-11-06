package com.tistory.blog.business.MemberService;

import com.tistory.blog.domain.dto.member.MemberDTO;
import com.tistory.blog.domain.dto.member.SignupDTO;
import com.tistory.blog.domain.entity.MemberEntity;
import com.tistory.blog.persistence.MemberRepository.MemberRepository;
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
    private final BCryptPasswordEncoder encoder;

    public MemberDTO Signup(SignupDTO signupDTO) {
        Optional<MemberEntity> existingMember = memberRepository.findByEmail(signupDTO.getEmail());
        if (existingMember.isPresent()) {
            throw new IllegalStateException("이미 가입된 이메일입니다.");
        }

        MemberEntity newMember = MemberEntity.builder()
                .email(signupDTO.getEmail())
                .phone(signupDTO.getPhone())
                .username(signupDTO.getUsername())
                .password(encoder.encode(signupDTO.getPassword()))
                .build();
        MemberEntity savedMember = memberRepository.save(newMember);
        return MemberDTO.of(savedMember);
    }
}
