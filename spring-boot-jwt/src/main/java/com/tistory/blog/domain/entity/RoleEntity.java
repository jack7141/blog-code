package com.tistory.blog.domain.entity;

import jakarta.persistence.*;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;

@Data
@NoArgsConstructor
@Entity
@Table(name = "role")
public class RoleEntity {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @Column(name = "name", nullable = false, unique = true)
    private String name; // e.g., "ADMIN", "USER"

    @Builder
    public RoleEntity(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return String.format("Role[id=%d, name='%s']", id, name);
    }
}
