# LLM API and Local Models

## Основные темы

- Устройство LLM API: токены, messages, usage, finish_reason
- Первый запрос через curl и SDK openai
- Настройки через pydantic-settings
- История диалога, цена запроса, ошибки и повторы
- Своя обёртка LLMClient
- Форматы API и провайдеры
- Параметры генерации
- Консольное приложение на Typer и Rich
- Локальные модели через Ollama и LM Studio
- Финальный проект: диалог двух моделей в терминале

## Быстрый старт

```bash
uv sync
```

`uv` сам установит Python 3.14 из файла `.python-version` и все зависимости.

Скопируйте `.env.example` в `.env` и впишите ключ API:

```bash
cp .env.example .env
```

| Переменная     | Значение по умолчанию     | Назначение                          |
|----------------|---------------------------|-------------------------------------|
| `LLM_API_KEY`  | нет, обязательна          | Ключ API провайдера                 |
| `LLM_BASE_URL` | `https://ollama.com/v1`   | Адрес OpenAI-совместимого API       |
| `LLM_MODEL`    | `gemma4:31b`              | Модель, которой отправляются запросы |

Файл `.env` в git не попадает. Чтобы сменить провайдера или перейти на локальную модель, меняйте только эти три значения.

Примеры запускаются из корня репозитория как модули:

```bash
uv run python -m src.modules.m1_llm_api_basics.l02_raw_json
```

## Программа

| Модуль                                  | Тема                          | Примеры                                                                                          |
|-----------------------------------------|-------------------------------|--------------------------------------------------------------------------------------------------|
| **1. Как устроен LLM API и первый запрос** | Токены                        | [Токены](src/modules/m1_llm_api_basics/l01_tokens.py)                                            |
|                                         | Сырой JSON                    | [Запрос без SDK](src/modules/m1_llm_api_basics/l02_raw_json.py)                                  |
|                                         | Первый запрос                 | [SDK openai](src/modules/m1_llm_api_basics/l03_first_call.py)                                    |
|                                         | Настройки                     | [Settings](src/settings.py)                                                                      |
|                                         | История диалога               | [Чат](src/modules/m1_llm_api_basics/l04_history.py)                                              |
|                                         | Цена запроса                  | [Расчёт по usage](src/modules/m1_llm_api_basics/l05_cost.py)                                     |
|                                         | Ошибки и лимиты               | [Повторы с паузой](src/modules/m1_llm_api_basics/l06_errors.py)                                  |

## Скрипты

### Линтеры

```bash
uv run ruff format src && uv run ruff check --fix src && uv run mypy src
```
