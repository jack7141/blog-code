package com.example.demo.config.oauth.provider;

import lombok.extern.slf4j.Slf4j;

import java.util.Map;

@Slf4j
public class KaKaoUserInfo implements OAuth2UserInfo {
    private Map<String, Object> attributes; // kakao 전체 응답

    public KaKaoUserInfo(Map<String, Object> attributes) {
        this.attributes = attributes;
        // 중요: 로그 추가
        log.info("KaKaoUser Attributes: {}", attributes);
    }

    @Override
    public String getProviderId() {
        return attributes.get("id").toString();
    }
    @Override
    public String getName() {
        Map<String, Object> kakaoAccount = (Map<String, Object>) attributes.get("kakao_account");
        if (kakaoAccount == null) return null;

        Map<String, Object> profile = (Map<String, Object>) kakaoAccount.get("profile");
        return profile != null ? (String) profile.get("nickname") : null;
    }

    @Override
    public String getEmail() {
        Map<String, Object> kakaoAccount = (Map<String, Object>) attributes.get("kakao_account");
        if (kakaoAccount == null) return null;

        Map<String, Object> profile = (Map<String, Object>) kakaoAccount.get("profile");
        return profile != null ? (String) profile.get("nickname") : null;
    }

    @Override
    public String getProvider() {
        return "kakao";
    }
}