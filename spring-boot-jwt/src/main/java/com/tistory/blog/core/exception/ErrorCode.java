package com.tistory.blog.core.exception;

import lombok.Getter;
import lombok.RequiredArgsConstructor;
import org.springframework.http.HttpStatus;

@Getter
@RequiredArgsConstructor
public enum ErrorCode {
//    DESTINATION_LOCKED(421, HttpStatus.Series.CLIENT_ERROR, "Destination Locked"),
//    UNPROCESSABLE_ENTITY(422, HttpStatus.Series.CLIENT_ERROR, "Unprocessable Entity"),
//    LOCKED(423, HttpStatus.Series.CLIENT_ERROR, "Locked"),
//    FAILED_DEPENDENCY(424, HttpStatus.Series.CLIENT_ERROR, "Failed Dependency"),
//    TOO_EARLY(425, HttpStatus.Series.CLIENT_ERROR, "Too Early"),
//    UPGRADE_REQUIRED(426, HttpStatus.Series.CLIENT_ERROR, "Upgrade Required"),
//    PRECONDITION_REQUIRED(428, HttpStatus.Series.CLIENT_ERROR, "Precondition Required"),
//    TOO_MANY_REQUESTS(429, HttpStatus.Series.CLIENT_ERROR, "Too Many Requests"),
//    REQUEST_HEADER_FIELDS_TOO_LARGE(431, HttpStatus.Series.CLIENT_ERROR, "Request Header Fields Too Large"),
//    UNAVAILABLE_FOR_LEGAL_REASONS(451, HttpStatus.Series.CLIENT_ERROR, "Unavailable For Legal Reasons"),
//    INTERNAL_SERVER_ERROR(500, HttpStatus.Series.SERVER_ERROR, "Internal Server Error"),
//    NOT_IMPLEMENTED(501, HttpStatus.Series.SERVER_ERROR, "Not Implemented"),
//    BAD_GATEWAY(502, HttpStatus.Series.SERVER_ERROR, "Bad Gateway"),
//    SERVICE_UNAVAILABLE(503, HttpStatus.Series.SERVER_ERROR, "Service Unavailable"),
//    GATEWAY_TIMEOUT(504, HttpStatus.Series.SERVER_ERROR, "Gateway Timeout"),
//    HTTP_VERSION_NOT_SUPPORTED(505, HttpStatus.Series.SERVER_ERROR, "HTTP Version not supported"),
//    VARIANT_ALSO_NEGOTIATES(506, HttpStatus.Series.SERVER_ERROR, "Variant Also Negotiates"),
//    INSUFFICIENT_STORAGE(507, HttpStatus.Series.SERVER_ERROR, "Insufficient Storage"),
//    LOOP_DETECTED(508, HttpStatus.Series.SERVER_ERROR, "Loop Detected"),
//    BANDWIDTH_LIMIT_EXCEEDED(509, HttpStatus.Series.SERVER_ERROR, "Bandwidth Limit Exceeded"),
//    NOT_EXTENDED(510, HttpStatus.Series.SERVER_ERROR, "Not Extended"),
//    NETWORK_AUTHENTICATION_REQUIRED(511, HttpStatus.Series.SERVER_ERROR, "Network Authentication Required");
    /*
     * 400 BAD_REQUEST: 잘못된 요청
     */
    BAD_REQUEST(HttpStatus.BAD_REQUEST, "Invalid request."),
    VALIDATION_ERROR(HttpStatus.BAD_REQUEST, "Validation failed."),

    /*
     * 401 UNAUTHORIZED: 인증되지 않은 사용자의 요청
     */
    UNAUTHORIZED_REQUEST(HttpStatus.UNAUTHORIZED, "Unauthorized."),

    /*
     * 403 FORBIDDEN: 권한이 없는 사용자의 요청
     */
    FORBIDDEN_ACCESS(HttpStatus.FORBIDDEN, "Forbidden."),

    /*
     * 404 NOT_FOUND: 리소스를 찾을 수 없음
     */
    NOT_FOUND(HttpStatus.NOT_FOUND, "Not found."),

    /*
     * 405 METHOD_NOT_ALLOWED: 허용되지 않은 Request Method 호출
     */
    METHOD_NOT_ALLOWED(HttpStatus.METHOD_NOT_ALLOWED, "Not allowed method."),

    /*
     * 500 INTERNAL_SERVER_ERROR: 내부 서버 오류
     */
    INTERNAL_SERVER_ERROR(HttpStatus.INTERNAL_SERVER_ERROR, "Server error.");

    private final HttpStatus httpStatus;
    private final String message;
}