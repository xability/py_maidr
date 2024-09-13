<div align="center">

<img src="https://github.com/xability/maidr/blob/main/logo/logo.svg" width="350px" alt="A stylized MAIDR logo, with curved characters for M A, a hand pointing for an I, the D character, and R represented in braille."/>

<hr style="color:transparent" />
<br />
</div>

# py-maidr

Python binder for maidr library

## Install and Upgrade

```sh
# install the latest release from PyPI
pip install -U maidr

# or install the development version from GitHub
pip install -U git+https://github.com/xability/py_maidr.git
```

## LLM Configuration for Interactive Shell

To use OpenAI or Gemini Models along with the maidr library, follow the steps below:

1. Signup and get the API Keys for OpenAI or Gemini Models.
2. Add the keys to environment variables so that python binder can access the keys.
   (Note: This only temporarily adds keys in environment variable, for persistent access you might want to add the export command to your shell configuration)

##### Mac Configuration

```bash
export OPENAI_API_KEY="<< add you key here >>"
export GEMINI_API_KEY="<< add you key here >>"
```

##### Windows Configuration

```
setx OPENAI_API_KEY "<< add you key here >>"
setx GEMINI_API_KEY "<< add you key here >>"
```

3. Run your python program.
