# LLM API and Local Models

## Main topics

- LLM API: tokens, messages, usage, finish_reason
- Chat history, request cost, errors and retries
- API formats and providers
- Generation parameters
- A console app with Typer and Rich
- Local models with Ollama and LM Studio

## Getting started

```bash
uv sync
```

```bash
cp .env.example .env
```

| Variable       | Default value           | 
|----------------|-------------------------|
| `LLM_API_KEY`  | required                | 
| `LLM_BASE_URL` | `https://ollama.com/v1` | 
| `LLM_MODEL`    | `gemma4:31b`            | 


```bash
uv run python -m src.modules.m1_llm_api_basics.l02_raw_json
```

## Program

| Module            | Topic             | Examples                                                                                                                                                                                                                       |
|-------------------|-------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **1. First call** | First calls       | [Request without SDK](src/modules/m1_llm_api_basics/l02_raw_json.py)  , [Request with openai SDK](src/modules/m1_llm_api_basics/l03_sdk_openai.py), [Request with ollama SDK](src/modules/m1_llm_api_basics/l04_sdk_ollama.py) |
|                   | Chat history      | [Chat history](src/modules/m1_llm_api_basics/l05_history.py)                                                                                                                                                                   |
|                   | Tokens            | [Tokens](src/modules/m1_llm_api_basics/l06_tokens.py), [Cost from usage](src/modules/m1_llm_api_basics/l07_cost.py)                                                                                                            |
|                   | Errors and limits | [Errors and limits](src/modules/m1_llm_api_basics/l08_errors.py)                                                                                                                                                            |

## Scripts

### Linters

```bash
uv run ruff format src && uv run ruff check --fix src && uv run mypy src
```
