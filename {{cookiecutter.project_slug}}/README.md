# `{{ cookiecutter.project_slug }}`

{{ cookiecutter.short_description }}

## Installation

First, [install Poetry](https://python-poetry.org/docs/#installation):

Linux/macOS

```bash
curl -sSL https://install.python-poetry.org | python3 -
```

Windows

```powershell
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | py -
```

Then install the `{{ cookiecutter.project_slug }}`:

```bash
poetry install
```

Activate the virtual environment created automatically by Poetry:

```bash
poetry shell
```
