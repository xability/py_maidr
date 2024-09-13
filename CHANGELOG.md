# CHANGELOG

## v0.9.0 (2024-09-13)

### Feature

* feat: fetch LLM API keys from user env variables (#102)

&lt;!-- Suggested PR Title: [feat/fix/refactor/perf/test/ci/docs/chore]
brief description of the change --&gt;
&lt;!-- Please follow Conventional Commits:
https://www.conventionalcommits.org/en/v1.0.0/ --&gt;

## Description
This pull request fixes the handling of API keys for LLMs in the code.
It adds a JavaScript script to handle the API keys for LLMs and
initializes the LLM secrets in the MAIDR instance. The script injects
the LLM API keys into the MAIDR instance and sets the appropriate
settings based on the presence of the Gemini and OpenAI API keys. This
ensures that the LLM functionality works correctly with the updated API
key handling.

closes #76 

## Type of Change

- [x] Bug fix
- [ ] New feature
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] Documentation update

## Checklist

- [x] My code follows the style guidelines of this project
- [x] I have performed a self-review of my code
- [x] I have commented my code, particularly in hard-to-understand areas
- [x] I have made corresponding changes to the documentation
- [x] My changes generate no new warnings
- [x] Any dependent changes have been merged and published in downstream
modules

# Pull Request

## Description
1. Added a new method called `initialize_llm_secrets()` in
environment.py which fetches the keys from the environment variable.
2. Injected the script when the maidr iframe loads initially.

## Checklist
&lt;!-- Please select all applicable options. --&gt;
&lt;!-- To select your options, please put an &#39;x&#39; in the all boxes that
apply. --&gt;

- [x] I have read the [Contributor Guidelines](../CONTRIBUTING.md).
- [x] I have performed a self-review of my own code and ensured it
follows the project&#39;s coding standards.
- [x] I have tested the changes locally following
`ManualTestingProcess.md`, and all tests related to this pull request
pass.
- [x] I have commented my code, particularly in hard-to-understand
areas.
- [x] I have updated the documentation, if applicable.
- [x] I have added appropriate unit tests, if applicable.

## Additional Notes
&lt;!-- Add any additional notes or comments here. --&gt;
&lt;!-- Template credit: This pull request template is based on Embedded
Artistry
{https://github.com/embeddedartistry/templates/blob/master/.github/PULL_REQUEST_TEMPLATE.md},
Clowder
{https://github.com/clowder-framework/clowder/blob/develop/.github/PULL_REQUEST_TEMPLATE.md},
and TalAter {https://github.com/TalAter/open-source-templates}
templates. --&gt; ([`fc84593`](https://github.com/xability/py_maidr/commit/fc84593a9b01904d24fd86da88f79e25db02417a))

## v0.8.0 (2024-08-27)

### Build

* build: remove `sphinx` from package dev dependencies ([`41f61a9`](https://github.com/xability/py_maidr/commit/41f61a915d9b3dea27419d984c8cd9408de794d5))

* build: move `black` formatter to `dev` dependencies ([`ca460b4`](https://github.com/xability/py_maidr/commit/ca460b4cca26418bee3cab2ce4949b96d5e60147))

### Feature

* feat: pick up seaborn heatmap fmt towards maidr (#90) ([`fb5dde0`](https://github.com/xability/py_maidr/commit/fb5dde0c7b2d65f6649342ff5474f032e4e36bae))

## v0.7.0 (2024-08-24)

## v0.6.0 (2024-08-21)

### Feature

* feat: support interactivity within ipython and quarto (#64) ([`620ddc9`](https://github.com/xability/py_maidr/commit/620ddc9d57175d5ca663d9dfaef4d2704809462f))

## v0.5.1 (2024-08-14)

### Fix

* fix: update poetry.lock (#74) ([`6216959`](https://github.com/xability/py_maidr/commit/621695940075fe195b0310c544c117bdc5a9d35e))

## v0.5.0 (2024-07-25)

### Feature

* feat: support hightlighing except for segmented plots and boxplots (#59) ([`c2cb99d`](https://github.com/xability/py_maidr/commit/c2cb99d8d7668b177dcf8b800b137eb994c85d6f))

## v0.4.2 (2024-07-02)

### Fix

* fix: seaborn multi plots in same session (#58) ([`c32fdfd`](https://github.com/xability/py_maidr/commit/c32fdfd32473dd354d292d33a19610a4c0a2eb63))

## v0.4.1 (2024-06-25)

## v0.4.0 (2024-06-16)

## v0.3.0 (2024-06-11)

### Fix

* fix: black formatting ci (#49) ([`20c4fa2`](https://github.com/xability/py_maidr/commit/20c4fa231bd5a78679cce7698d2a42077c97f330))

* fix: remove docs (#48) ([`9b8cae5`](https://github.com/xability/py_maidr/commit/9b8cae5c1e4071be6edbfdbab8f4b498516f9caf))

## v0.2.0 (2024-05-16)

### Documentation

* docs: add quarto and quartodoc for static website (#38)

`_quarto.yml` includes the base structure of the static website with a navbar and the main site.  The navbar includes &#39;Overview&#39;, &#39;Get Started&#39;, and &#39;API Referece&#39; sections, which are structured in `_index.qmd`, `_get_started.qmd`, and the quartodoc section of `_quarto.yml` respectively. Currently, the &#39;Overview&#39; and &#39;Get Started&#39; sections are left empty, which will be generated in the upcoming releases. The &#39;API Reference&#39; section will include the docstring in a neat format generated by `quartodoc`.

Resolves: #17 ([`011b1b2`](https://github.com/xability/py_maidr/commit/011b1b2b916df3036644d43cd6741f663ca64bc3))

* docs: add docstring (#34) ([`59f0ca1`](https://github.com/xability/py_maidr/commit/59f0ca1551643f9077fe2891af153e5038ddefe8))

### Feature

* feat: use htmltools instead of str (#33)

* feat: use htmltools instead of str

* feat: show html using htmltools

* chore: move mixin to utils package ([`8b0a838`](https://github.com/xability/py_maidr/commit/8b0a838bf7cd73ecd5e036d9be28e8ed0523a9ed))

## v0.1.2 (2024-05-13)

### Documentation

* docs: add documentation for classes and methods (#16)

* docs: add documentation for classes and methods, following numpy docstring style

* fix: convert maidr data to numpy array

* docs: add docstring

* chore: change | none to optional typing

* chore: rever to | none typing

---------

Co-authored-by: SaaiVenkat &lt;greenghost1100@gmail.com&gt; ([`4b5387e`](https://github.com/xability/py_maidr/commit/4b5387e0026b375e37e9097a4abaad7c8d110f94))

* docs: update installation instructions in README.md ([`a5134ed`](https://github.com/xability/py_maidr/commit/a5134ed20d544220cee4f89ae132b750a8005807))

* docs: update py-maidr installation instructions ([`0185aec`](https://github.com/xability/py_maidr/commit/0185aece83c66a85baea3d0ff4a9abbb6fa2f771))

* docs: add development environment setup instructions ([`36ecba2`](https://github.com/xability/py_maidr/commit/36ecba242c680b9ed5e405d6e3924dd3c0b88b0c))

* docs: add CONTRIBUTING.md file ([`2e4cf10`](https://github.com/xability/py_maidr/commit/2e4cf10800d75773e87981fb1665430c7c0a1306))

* docs: add code of conduct ([`777f850`](https://github.com/xability/py_maidr/commit/777f85088e49f3be3faa2e10cc3f6bce14c168b8))

* docs: add CHANGELOG file ([`f19c78c`](https://github.com/xability/py_maidr/commit/f19c78c6c80cb5050765bbe6b7154dbe3a80dc17))

### Feature

* feat: support seaborn bar and count plot (#12) ([`fd622bd`](https://github.com/xability/py_maidr/commit/fd622bdd51236627cd37babf9e20ef1378311ff7))

* feat: redesign python binder (#10)

* feat: redesign python binder

* docs: add example bar plot ([`2fe4901`](https://github.com/xability/py_maidr/commit/2fe490158c7cba8fb40d939a079e4c0817ed349a))

### Fix

* fix: support seaborn breaking changes (#31) ([`afe5382`](https://github.com/xability/py_maidr/commit/afe538209e313f7a42c355c7234ba5f1d1ebf97b))

* fix: update pyproject.toml version and htmltools dependency (#14) ([`fcaca48`](https://github.com/xability/py_maidr/commit/fcaca486dff79ac6861d9561986088f432d74b64))
