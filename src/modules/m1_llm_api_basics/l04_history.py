"""Урок 4. Модель не помнит прошлых запросов: историю присылаем мы.
Запуск: uv run python -m src.modules.m1_llm_api_basics.l04_history
"""

from openai import OpenAI
from openai.types.chat import ChatCompletionMessageParam

from src.settings import Settings

Message = ChatCompletionMessageParam


def ask(client: OpenAI, model: str, messages: list[Message]) -> str:
    completion = client.chat.completions.create(model=model, messages=messages)
    return completion.choices[0].message.content or ""


def chat(client: OpenAI, model: str) -> None:
    history: list[Message] = [
        {"role": "system", "content": "Ты дружелюбный помощник, отвечай кратко."}
    ]
    while user_text := input("Вы: ").strip():
        history.append({"role": "user", "content": user_text})
        answer = ask(client, model, history)
        history.append({"role": "assistant", "content": answer})
        print(f"Модель: {answer}")
        print(f"[Сообщений в истории: {len(history)}]")


def main() -> None:
    settings = Settings()
    client = OpenAI(api_key=settings.llm_api_key, base_url=settings.llm_base_url)
    chat(client, settings.llm_model)


if __name__ == "__main__":
    main()
