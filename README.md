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

`uv` installs Python 3.14 (set in `.python-version`) and all dependencies for you.

Copy `.env.example` to `.env` and add your API key:

```bash
cp .env.example .env
```

| Variable       | Default                 | What it is                              |
|----------------|-------------------------|-----------------------------------------|
| `LLM_API_KEY`  | none, required          | API key from your provider              |
| `LLM_BASE_URL` | `https://ollama.com/v1` | Address of the OpenAI-compatible API    |
| `LLM_MODEL`    | `gemma4:31b`            | Model that receives your requests       |

The `.env` file is not committed to git. To use another provider or a local model, change only these three values.

Run the examples from the root of the repository, as modules:

```bash
uv run python -m src.modules.m1_llm_api_basics.l02_raw_json
```

## Program

| Module            | Topic             | Examples                                                            |
|-------------------|-------------------|---------------------------------------------------------------------|
| **1. First call** | Raw JSON          | [Request without SDK](src/modules/m1_llm_api_basics/l02_raw_json.py) |
|                   | SDK               | [openai SDK](src/modules/m1_llm_api_basics/l03_sdk_openai.py)       |
|                   |                   | [ollama SDK](src/modules/m1_llm_api_basics/l04_sdk_ollama.py)       |
|                   | Settings          | [Settings](src/settings.py)                                         |
|                   | Chat history      | [Chat](src/modules/m1_llm_api_basics/l05_history.py)                |
|                   | Tokens            | [Tokens](src/modules/m1_llm_api_basics/l06_tokens.py)               |
|                   | Request cost      | [Cost from usage](src/modules/m1_llm_api_basics/l07_cost.py)        |
|                   | Errors and limits | [Retries with a pause](src/modules/m1_llm_api_basics/l08_errors.py) |

## Scripts

### Linters

```bash
uv run ruff format src && uv run ruff check --fix src && uv run mypy src
```
