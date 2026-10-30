"""Урок 2. Запрос Chat Completions на сыром JSON.
Запуск: uv run python -m src.modules.m1_llm_api_basics.l02_raw_json
"""

import json

import httpx

from src.settings import Settings


def main() -> None:
    settings = Settings()
    payload = {
        "model": settings.llm_model,
        "messages": [
            {"role": "system", "content": "Ты отвечаешь одним коротким предложением."},
            {"role": "user", "content": "Какая LLM самая крутая?"},
        ],
    }
    print("ЗАПРОС")
    print(json.dumps(payload, ensure_ascii=False, indent=2))

    response = httpx.post(
        f"{settings.llm_base_url}/chat/completions",
        headers={"Authorization": f"Bearer {settings.llm_api_key}"},
        json=payload,
        timeout=60,
    )
    response.raise_for_status()
    body = response.json()

    print("\nОТВЕТ")
    print(json.dumps(body, ensure_ascii=False, indent=2))

    choice = body["choices"][0]
    print("\nТекст:", choice["message"]["content"])
    print("finish_reason:", choice["finish_reason"])
    print("usage:", body["usage"])


if __name__ == "__main__":
    main()
