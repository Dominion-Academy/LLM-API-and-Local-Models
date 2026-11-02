"""
Запуск: uv run python -m src.check_env
"""

import sys

from openai import APIConnectionError, APIStatusError
from pydantic import ValidationError

from src.llm_client import LLMClient
from src.settings import ENV_FILE, Settings


def main() -> int:
    try:
        settings = Settings()
    except ValidationError:
        print(
            f"Не найдена LLM_API_KEY. Проверьте, что в файле {ENV_FILE} есть строка LLM_API_KEY=..."
        )
        return 1

    client = LLMClient(settings, max_attempts=1)
    try:
        client.chat([{"role": "user", "content": "Ответь одним словом: привет"}])
    except APIConnectionError:
        print("Не удалось подключиться. Проверьте LLM_BASE_URL и интернет.")
        return 1
    except APIStatusError as error:
        print(f"Сервер ответил ошибкой {error.status_code}. Проверьте LLM_API_KEY и LLM_MODEL.")
        return 1
    except RuntimeError as error:
        print(f"Запрос не прошёл: {error}. Проверьте LLM_BASE_URL.")
        return 1

    print("Всё окей: запрос к LLM выполнен, настройки в .env верные.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
