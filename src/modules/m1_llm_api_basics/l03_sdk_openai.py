"""Урок 3. SDK openai: запрос из прошлого урока без ручной работы с HTTP.
Запуск: uv run python -m src.modules.m1_llm_api_basics.l03_sdk_openai
"""

from openai import OpenAI

from src.settings import Settings


def main() -> None:
    settings = Settings()
    client = OpenAI(api_key=settings.llm_api_key, base_url=settings.llm_base_url)

    completion = client.chat.completions.create(
        model=settings.llm_model,
        messages=[
            {"role": "system", "content": "Ты отвечаешь одним коротким предложением."},
            {"role": "user", "content": "Какая LLM самая крутая?"},
        ],
    )

    choice = completion.choices[0]
    print("Текст:", choice.message.content)
    print("finish_reason:", choice.finish_reason)
    print("usage:", completion.usage)


if __name__ == "__main__":
    main()
