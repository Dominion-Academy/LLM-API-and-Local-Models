"""Урок 6. Ошибки API и повтор запроса с экспоненциальной паузой.
Запуск: uv run python -m src.modules.m1_llm_api_basics.l06_errors
"""

import time

from openai import (
    APIConnectionError,
    APIStatusError,
    OpenAI,
    RateLimitError,
)

from src.settings import Settings


def ask_with_retries(client: OpenAI, model: str, prompt: str, max_attempts: int = 4) -> str:
    for attempt in range(1, max_attempts + 1):
        try:
            completion = client.chat.completions.create(
                model=model, messages=[{"role": "user", "content": prompt}], max_tokens=100
            )
            return completion.choices[0].message.content or ""
        except (RateLimitError, APIConnectionError) as error:
            reason = type(error).__name__
        except APIStatusError as error:
            if error.status_code < 500:
                raise
            reason = f"ошибка сервера {error.status_code}"
        if attempt == max_attempts:
            raise RuntimeError(f"Не удалось получить ответ за {max_attempts} попыток")
        pause = 2 ** (attempt - 1)  # 1, 2, 4, 8...
        print(f"Попытка {attempt} не удалась ({reason}), жду {pause} с")
        time.sleep(pause)
    raise AssertionError("недостижимо")


def main() -> None:
    settings = Settings()
    client = OpenAI(api_key=settings.llm_api_key, base_url=settings.llm_base_url, max_retries=0)
    print(ask_with_retries(client, settings.llm_model, "Как дела?"))


if __name__ == "__main__":
    main()
