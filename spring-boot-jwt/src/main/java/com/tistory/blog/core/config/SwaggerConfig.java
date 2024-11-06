package com.tistory.blog.core.config;

import io.swagger.v3.oas.models.Components;
import io.swagger.v3.oas.models.OpenAPI;
import io.swagger.v3.oas.models.info.Info;
import io.swagger.v3.oas.models.security.SecurityRequirement;
import io.swagger.v3.oas.models.security.SecurityScheme;
import lombok.RequiredArgsConstructor;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

@Configuration
@RequiredArgsConstructor
public class SwaggerConfig {

    @Bean
    public OpenAPI openAPI() {
        Info info = new Info()
                .version("ver.1.0.0")
                .title("우주를 놀라게 하자: 📚 블로그 백엔드 JWT 학습 API ")
                .description("블로그 백엔드 API 공부");

        // Define JWT Bearer token security scheme
        SecurityScheme securityScheme = new SecurityScheme()
                .name("Bearer Authentication")
                .type(SecurityScheme.Type.HTTP)
                .scheme("bearer")
                .bearerFormat("JWT");

        return new OpenAPI()
                .components(new Components().addSecuritySchemes("bearerAuth", securityScheme)) // Add the security scheme globally
                .info(info)
                .addSecurityItem(new SecurityRequirement().addList("bearerAuth"));  // Apply security globally to all APIs
    }
}
