"""LLM exceptions module"""

from typing import Any


class LLMError(Exception):
    """Base exception for LLM errors"""

    def __init__(self, message: str, cause: Exception | None = None) -> None:
        """Initialize LLM error

        Args:
            message: Error message
            cause: Original exception that caused this error

        Raises:
            ValueError: If message is empty
        """
        if not message:
            raise ValueError("Message cannot be empty")
        super().__init__(message)
        self._message = message
        self._cause = cause

    @property
    def message(self) -> str:
        """Get error message"""
        return self._message

    @property
    def cause(self) -> Exception | None:
        """Get original exception"""
        return self._cause

    def __str__(self) -> str:
        """Get string representation"""
        return self._message

    def __repr__(self) -> str:
        """Get detailed string representation"""
        return f"{self.__class__.__name__}('{self._message}')"

    def __eq__(self, other: Any) -> bool:
        """Check equality"""
        if not isinstance(other, self.__class__):
            return False
        return self._message == other._message

    def __hash__(self) -> int:
        """Get hash value"""
        return hash(self._message)


class ModelNotFoundError(LLMError):
    """Error when model is not found"""

    def __init__(self, model_name: str) -> None:
        """Initialize error"""
        super().__init__(f"Model not found: {model_name}")


class TokenLimitError(LLMError):
    """Error when token limit is exceeded"""

    def __init__(self, max_tokens: int, actual_tokens: int) -> None:
        """Initialize error"""
        if max_tokens < 0 or actual_tokens < 0:
            raise ValueError("Token counts must be non-negative")
        super().__init__(
            f"Token limit exceeded: {actual_tokens} tokens (max: {max_tokens})"
        )


class PromptError(LLMError):
    """Error with prompt format or content"""

    def __init__(self, message: str) -> None:
        """Initialize error"""
        super().__init__(f"Invalid prompt: {message}")


class ResponseError(LLMError):
    """Error with response format or content"""

    def __init__(self, message: str) -> None:
        """Initialize error"""
        super().__init__(f"Invalid response: {message}")


class RateLimitError(LLMError):
    """Error when rate limit is exceeded"""

    def __init__(self, message: str) -> None:
        """Initialize error"""
        super().__init__(f"Rate limit exceeded: {message}")


class AuthenticationError(LLMError):
    """Error with authentication"""

    def __init__(self, message: str) -> None:
        """Initialize error"""
        super().__init__(f"Authentication error: {message}")
