package com.example.demo.config.auth;

import com.example.demo.model.User;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.oauth2.core.user.OAuth2User;

import java.io.Serializable;
import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Map;

// 시큐리티가 /login 주소 요청이 오면 낚아채서 로그인을 진행시킴
// 로그인이 진행이 완료가 되면 시큐리티 session을 만들어준다
public class PrincipalDetails implements UserDetails, OAuth2User, Serializable {
    private static final long serialVersionUID = 1L;
    private User user;
    private Map<String, Object> attributes;

    // 일반 시큐리티 로그인시 사용
    public PrincipalDetails(User user) {
        this.user = user;
    }

    // 일반 시큐리티 로그인시 사용
    public PrincipalDetails(User user, Map<String, Object> attributes) {
        this.user = user;
        this.attributes = attributes;
    }

    public User getUser() {
        return user;
    }

    @Override
    public Collection<? extends GrantedAuthority> getAuthorities() {
//        해당 User의 권한을 리턴하는 곳
        Collection<GrantedAuthority> collet = new ArrayList<GrantedAuthority>();
        collet.add(()->{ return user.getRole();});
        return collet;
    }

    @Override
    public String getPassword() {
        return user.getPassword();
    }

    @Override
    public String getUsername() {
        return user.getUsername();
    }

    @Override
    public boolean isAccountNonExpired() {
        return true;  // 계정 만료 여부
    }

    @Override
    public boolean isAccountNonLocked() {
        return true;  // 계정 잠금 여부
    }

    @Override
    public boolean isCredentialsNonExpired() {
        return true;  // 비밀번호 만료 여부
    }

    @Override
    public boolean isEnabled() {
        return true;  // 계정 활성화 여부
    }

    // OAuth2User 인터페이스 구현
    @Override
    public Map<String, Object> getAttributes() {
        return attributes;
    }

    @Override
    public String getName() {
        return user.getId() + "";
    }

}
