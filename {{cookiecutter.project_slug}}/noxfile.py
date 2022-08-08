import nox
from nox_poetry import Session, session

nox.options.error_on_external_run = True
nox.options.reuse_existing_virtualenvs = True
nox.options.sessions = ["fmt_check", "lint", "type_check", "test"]


@session(python=["3.9", "3.10"])
def test(s: Session) -> None:
    s.install(".", "pytest", "pytest-cov")
    s.run(
        "python",
        "-m",
        "pytest",
        "--cov={{ cookiecutter.module_name }}",
        "--cov-report=html",
        "--cov-report=term",
        "tests",
        *s.posargs,
    )


# For some sessions, set venv_backend="none" to simply execute scripts within the existing Poetry
# environment. This requires that nox is run within `poetry shell` or using `poetry run nox ...`.
@session(venv_backend="none")
def fmt(s: Session) -> None:
    s.run("isort", "src", "tests")
    s.run("black", "src", "tests")


@session(venv_backend="none")
def fmt_check(s: Session) -> None:
    s.run("isort", "--check", "src", "tests")
    s.run("black", "--check", "src", "tests")


@session(venv_backend="none")
def lint(s: Session) -> None:
    s.run("pflake8", "src", "tests")


@session(venv_backend="none")
def type_check(s: Session) -> None:
    s.run("mypy", "src", "tests", "noxfile.py")
