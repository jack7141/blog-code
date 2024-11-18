package com.tistory.blog.core.exception;

public class DuplicateMemberException extends RuntimeException{
    public DuplicateMemberException(String message) {
        super(message);
    }
}
