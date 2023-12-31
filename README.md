<h1 align="center">Python file checker service
<div align="center">
<a href="https://github.com/pre-commit/pre-commit"><img alt="pre-commit" src="https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit"/></a>
<a href="https://github.com/psf/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
<a href="https://pycqa.github.io/isort/"><img alt="Imports: isort" src="https://img.shields.io/badge/%20imports-isort-%231674b1?style=flat"></a>
<a href="https://github.com/pylint-dev/pylint"><img alt="pylint" src="https://img.shields.io/badge/linting-pylint-yellowgreen"></a>
</div>
</h1>
<div align="center">
<img height="300" width="300" alt="Python File Checker" src="images/logo.svg"/>
</div>

## Link to site

https://skyeng-test-task.xyz/


## Description

Code Quality Checker: This service automates the evaluation
of Python code against industry-standard coding conventions
such as PEP 8. It efficiently assesses your codebase,
highlighting deviations from best practices and offering
insights for improved code readability and maintainability.


## Launching
#### Dev

Create `.env` file and populate it with credentials.

Then run `docker compose` command to launch dev version:
```shell
docker compose -f docker-compose.yaml -f docker-compose.local.yaml --env-file ./.env up -d --build
```
