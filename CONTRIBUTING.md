
# Code Contribution

To contribute to this repository, please follow the steps below to set up your development environment.

First, install all the recommended VSCode extensions for this workspace when prompted.

Second, install poetry:

``` sh
pip install poetry

# In the project root directory
poetry install
```

Third, install pre-commit hooks which will automatically reformat and lint the code when you make a commit:

``` sh
poetry run pre-commit install
```
