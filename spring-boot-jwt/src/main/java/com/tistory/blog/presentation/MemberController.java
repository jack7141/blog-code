package com.tistory.blog.presentation;

import com.tistory.blog.business.MemberService.MemberService;
import com.tistory.blog.domain.dto.member.MemberDTO;
import com.tistory.blog.domain.dto.Request.SignupDTO;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.tags.Tag;
import jakarta.validation.Valid;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

@RestController
@RequiredArgsConstructor
@RequestMapping("/api/v1/member")
@Tag(name = "사용자", description = "사용자 관련 API")
public class MemberController {

    private final MemberService memberService;

    @Operation(summary = "회원 가입")
    @PostMapping("/signup")
    public ResponseEntity<MemberDTO> CreateMember(@Valid @RequestBody SignupDTO signupDTO) {
        MemberDTO newMember = memberService.Signup(signupDTO);
        return ResponseEntity.status(201).body(newMember);
    }
}
