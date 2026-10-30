import time
from dataclasses import dataclass
from typing import Any

from openai import APIConnectionError, APIStatusError, OpenAI, RateLimitError
from openai.types.chat import ChatCompletionMessageParam

from src.settings import Settings

Message = ChatCompletionMessageParam


@dataclass(frozen=True)
class ChatResult:
    text: str
    finish_reason: str
    prompt_tokens: int
    completion_tokens: int


class LLMClient:
    def __init__(
        self,
        settings: Settings,
        *,
        timeout: float = 60.0,
        max_attempts: int = 4,
    ) -> None:
        self.settings = settings
        self.max_attempts = max_attempts
        self._client = OpenAI(
            api_key=self.settings.llm_api_key,
            base_url=self.settings.llm_base_url,
            timeout=timeout,
            max_retries=0,  # повторы делаем сами в chat(), поэтому встроенные повторы отключаем
        )

    def chat(
        self,
        messages: list[Message],
        *,
        model: str | None = None,
        **kwargs: Any,
    ) -> ChatResult:
        for attempt in range(1, self.max_attempts + 1):
            try:
                completion = self._client.chat.completions.create(
                    model=model or self.settings.llm_model,
                    messages=messages,
                    **kwargs,
                )
                break  # выходим из цикла попыток, если успешно вернулся ответ
            except RateLimitError, APIConnectionError:
                pass
            except APIStatusError as error:
                if error.status_code < 500:
                    raise
            if attempt == self.max_attempts:
                raise RuntimeError(f"Нет ответа после {self.max_attempts} попыток")
            time.sleep(2 ** (attempt - 1))

        choice = completion.choices[0]
        usage = completion.usage
        return ChatResult(
            text=choice.message.content or "",
            finish_reason=choice.finish_reason,
            prompt_tokens=usage.prompt_tokens if usage else 0,
            completion_tokens=usage.completion_tokens if usage else 0,
        )
