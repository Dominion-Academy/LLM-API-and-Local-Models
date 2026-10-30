"""Урок 3. Первый запрос через SDK openai.
Запуск: uv run python -m src.modules.m1_llm_api_basics.l03_first_call
"""

from openai import OpenAI

from src.settings import Settings


def main() -> None:
    settings = Settings()
    client = OpenAI(api_key=settings.llm_api_key, base_url=settings.llm_base_url)

    completion = client.chat.completions.create(
        model=settings.llm_model,
        messages=[{"role": "user", "content": "Объясни, что такое токен, в двух предложениях."}],
        max_tokens=300,
    )

    print(completion.choices[0].message.content)
    print("finish_reason:", completion.choices[0].finish_reason)
    print("usage:", completion.usage)


if __name__ == "__main__":
    main()
