# Contributing to `py-maidr`

Thank you for your interest in contributing to maidr project! We welcome contributions from everyone.

# Pre-requisites

To contribute to this project, you need to have the following installed on your local machine:

1. git

2. python (version 3.8 or higher is required)

3. poetry

4. make

# Get Started!

Ready to contribute? Here's how to set up `py-maidr` for local development.
Please note this documentation assumes you already have `poetry` and `Git` installed and ready to go.

1. Fork the `py-maidr` repo on GitHub.

2. Clone your fork locally:

    ```bash
    cd <directory_in_which_repo_should_be_created>
    git clone git@github.com:YOUR_NAME/py-maidr.git
    ```

3. Now we need to install the environment. Navigate into the directory

    ```bash
    cd py-maidr
    ```

    If you are using `pyenv`, select a version to use locally. (See installed versions with `pyenv versions`)

    ```bash
    pyenv local <x.y.z>
    ```

4. Then, install and activate the environment with:

    ```bash
    poetry install
    poetry shell
    ```

5. Install pre-commit to run linters/formatters at commit time:

    ```bash
    poetry run pre-commit install
    ```

6. Install the [`commit-msg`](https://pre-commit.com/#pre-commit-for-commit-messages) hook in your project repo:

    ```bash
    pre-commit install --hook-type commit-msg
    ```

7. Alternatively, if you have installed [`make`](https://www.gnu.org/software/make/#download), you can do step 4, 5, 6 in one go

    ```bash
    make install
    ```

8. Create a branch for local development:

    ```bash
    git checkout -b name-of-your-bugfix-or-feature
    ```

    Now you can make your changes locally.

9. Don't forget to add test cases for your added functionality to the `tests` directory.

10. When you're done making changes, check that your changes pass the formatting tests.

    ```bash
    make check
    ```

    Now, validate that all unit tests are passing:

    ```bash
    make test
    ```

11. Before raising a pull request you should also run tox.
   This will run the tests across different versions of Python:

    ```bash
    tox
    ```

    This requires you to have multiple versions of python installed.
    This step is also triggered in the CI/CD pipeline, so you could also choose to skip this step locally.

12. Committing Your Changes

- We use [conventional commits](https://www.conventionalcommits.org/) to maintain a clear and consistent commit history. Here's how to write a conventional commit message:

  #### Format

  - Each commit message should follow this format: `<type>[optional scope]: <description>`

  - **Types**: Describes the type of change you're making. Common types include:
    - `feat`: Introduces a new feature.
    - `fix`: Fixes a bug.
    - `docs`: Documentation changes.
    - `style`: Code style changes (formatting, missing semi-colons, etc. – does not affect code logic).
    - `refactor`: Code changes that neither fixes a bug nor adds a feature.
    - `perf`: Performance improvements.
    - `test`: Adding or correcting tests.
    - `chore`: Routine tasks, maintenance, and other non-production changes.
    - `ci`: Changes to our CI configuration files and scripts, specifically for GitHub Actions.
  - **Scope**: (Optional) A word or two describing where the change happens, like `login`, `signup`, etc.
  - **Description**: A succinct description of the change in lowercase.

  #### Denoting a Breaking Change

  - To denote a breaking change, include an exclamation mark `!` before the colon.
  - Example: `feat(database)!: remove deprecated methods`

  #### Mentioning Issue Numbers

  - If your commit addresses a specific issue, mention the issue number at the end of the commit message.
  - Example: `fix(file-upload): correct MIME type handling, closes #123`

  #### Examples

  - `feat(authentication): add JWT token support`
  - `fix(api): resolve data retrieval issue`
  - `docs(readme): update installation instructions`
  - `style(header): adjust layout spacing`
  - `refactor(user-profile): streamline user data processing`
  - `perf(image-loading): optimize image caching`
  - `chore(dependencies): update lodash to 4.17.21`
  - `test(login): add additional unit tests for password reset`
  - `ci(github-actions): update build and deployment workflow`

  #### Commit Message Linting

  - When you commit your changes, Pre-commit and Ruff will automatically check your commit messages.
  - If your message does not meet the conventional commit format, the commit will be rejected, and you'll need to modify the message.

# Code of Conduct

Please note that this project is released with a Contributor Code of Conduct. By participating in this project you agree to abide by its terms.
