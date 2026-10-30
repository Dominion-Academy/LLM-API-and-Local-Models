"""Урок 5. Цена запроса по полю usage.
Запуск: uv run python -m src.modules.m1_llm_api_basics.l05_cost
"""

from openai import OpenAI

from src.settings import Settings

# Условные тарифы в долларах за миллион токенов.
PRICE_INPUT_PER_MILLION = 0.50
PRICE_OUTPUT_PER_MILLION = 2.00


def calculate_cost(prompt_tokens: int, completion_tokens: int) -> float:
    prompt_cost = prompt_tokens * PRICE_INPUT_PER_MILLION / 1_000_000
    completion_cost = completion_tokens * PRICE_OUTPUT_PER_MILLION / 1_000_000
    return prompt_cost + completion_cost


def main() -> None:
    settings = Settings()
    client = OpenAI(api_key=settings.llm_api_key, base_url=settings.llm_base_url)

    completion = client.chat.completions.create(
        model=settings.llm_model,
        messages=[
            {"role": "user", "content": "Расскажи какой язык программирования учить в 2027?."}
        ],
    )
    usage = completion.usage
    if usage is None:
        raise RuntimeError("Сервер не вернул данные об использованных токенах")

    cost = calculate_cost(usage.prompt_tokens, usage.completion_tokens)
    print(f"Вход: {usage.prompt_tokens} токенов, выход: {usage.completion_tokens} токенов")
    print(f"Цена запроса: ${cost:.6f}")
    print(f"Тысяча таких запросов: ${cost * 1000:.2f}")


if __name__ == "__main__":
    main()
