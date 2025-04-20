package com.example.demo.config.auth;

import com.example.demo.model.User;
import com.example.demo.repository.UserRepository;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Service;

// 시큐리티 설정에서 loginProcessingUrl("/login")
// login 요청이 오면 자동으로 UserDetailsService 타입으로 IoC되어있는 loadUserByUsername 함수가 실행 규칙임
@Service
@Slf4j
public class PrincipalDetailsService  implements UserDetailsService {
    @Autowired
    private UserRepository userRepository;
    //  내부에 있는 username은 외부에서 들어오는 값과 동일해야함 만약 바꾸고 싶으면, 시큐리티 config에서 usernameparams로 바꿔야함
    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        log.info("loadUserByUsername {}", username);
        User user = userRepository.findByUsername(username);
        log.info("User 객체를 찾았습니다: {}", user);
        if(user == null) {
            throw new UsernameNotFoundException("사용자를 찾을 수 없습니다: " + username);
        } else {
            return new PrincipalDetails(user);
        }
    }
}
