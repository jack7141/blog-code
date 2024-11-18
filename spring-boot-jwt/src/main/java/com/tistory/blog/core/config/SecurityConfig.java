package com.tistory.blog.core.config;

import jakarta.servlet.http.HttpServletRequest;
import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.annotation.web.configuration.WebSecurityCustomizer;
import org.springframework.security.config.annotation.web.configurers.AbstractHttpConfigurer;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
/**
 * [Spring Security Config 클래스]
 */
@Configuration // 이 클래스가 Spring의 구성 클래스임을 나타내며. Spring Security 설정을 포함한다.
@RequiredArgsConstructor
@EnableWebSecurity //  Spring Security를 활성화시킨다.
public class SecurityConfig {

    /*
    *  인증 없이 Swagger 엔드포인트에 계속 액세스
    * */
    @Bean
    public WebSecurityCustomizer webSecurityCustomizer() {
        return web -> web.ignoring()
                .requestMatchers("/swagger-ui/**", "/swagger-resources/**", "/v3/api-docs");
    }


    /*
    * 향후 인가, 허가를 위해 설정
    * */
    @Bean
    public SecurityFilterChain securityFilterChain(HttpSecurity http) throws Exception{
        /*
        * Session 방식이 아니라 JWT 방식을 활용할 예정이기 때문에, Session 정책을 비활성화 시켜준다.
        * */
        http
                .sessionManagement(management -> management.sessionCreationPolicy(SessionCreationPolicy.STATELESS));

        /*
        * Session 정책을 사용하지 않으므로 CSRF(Cross-Site Request Forgery)을 사용하지 않으므로 비활성화 시켜준다.
        * */
        http
                .csrf(AbstractHttpConfigurer::disable);


        /* H2 콘솔 프레임 옵션을 위해 추가 설정
         * */
        http
                .headers(headers -> headers
                        .frameOptions(frameOptions -> frameOptions.sameOrigin())
                );

        return http.build();
    }

    /*
    *  비밀번호를 암호화하는 데 사용되는 해시 방식이다. 해당 암호화 방식을 Bean으로 저장하여 다른 클래스에서 사용 가능하도록 한다.
    * */
    @Bean
    public BCryptPasswordEncoder passwordEncoder() {
        /*
        * BCrypt 알고리즘 활용
        * */
        return new BCryptPasswordEncoder();
    }

    @Bean
    public AuthenticationManager authenticationManager(AuthenticationConfiguration authenticationConfiguration) throws Exception {
        return authenticationConfiguration.getAuthenticationManager();
    }
}
