"""Урок 3. SDK ollama: тот же запрос через собственный API Ollama.
Запуск: uv run python -m src.modules.m1_llm_api_basics.l04_sdk_ollama
"""

from ollama import Client

from src.settings import Settings


def main() -> None:
    settings = Settings()

    client = Client(host="https://ollama.com", headers={"Authorization": f"Bearer {settings.llm_api_key}"})

    response = client.chat(
        model=settings.llm_model,
        messages=[
            {"role": "system", "content": "Ты отвечаешь одним коротким предложением."},
            {"role": "user", "content": "Какая LLM самая крутая?"},
        ],
    )

    print("Текст:", response.message.content)
    print("done_reason:", response.done_reason)
    print("prompt_eval_count:", response.prompt_eval_count)
    print("eval_count:", response.eval_count)


if __name__ == "__main__":
    main()
