# Basic Python Template

> [python-blueprint](https://github.com/johnthagen/python-blueprint) ❤️
> [cookiecutter-poetry](https://github.com/timhughes/cookiecutter-poetry)

Данный репозиторий представляет из себя шаблон проекта `Python` для быстрой разработки
(в частности, в условиях очень сжатых сроков, например, на хакатонах).

В качестве **package manager** используется [poetry](https://python-poetry.org),
для проведения автоматических тестов используется [nox](https://nox.thea.codes),
а для создания документации - [mkdocs](https://www.mkdocs.org).
Также уже настроены автоматические Github Actions.

## Использование

1. Установите `cookiecutter`:

   ```bash
    pip install cookiecutter
   ```

2. Запустите `cookiecutter`, указав ссылку на этот репозиторий:

   ```bash
   cookiecutter gh://github.com/sostema/basic-python-template
   ```

3. В интерактивном режиме создайте проект с нужными Вам настройками.
4. Поздравляю! Вы молодцы!
