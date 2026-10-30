"""Урок 1. Как текст превращается в токены.
Запуск: uv run python -m src.modules.m1_llm_api_basics.l01_tokens
"""

import tiktoken

TEXTS = [
    "Hello, world!",
    "Привет, мир!",
    "LLM API and Local Models",
    "def add(a, b): return a + b",
]


def main() -> None:
    encoding = tiktoken.get_encoding("o200k_base")
    for text in TEXTS:
        token_ids = encoding.encode(text)
        pieces = [encoding.decode([token_id]) for token_id in token_ids]
        print(f"\n{text!r}: {len(text)} символов, {len(token_ids)} токенов")
        print(f"- id:     {token_ids}")
        print(f"- фрагменты:  {pieces}")


if __name__ == "__main__":
    main()
