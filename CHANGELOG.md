# CHANGELOG

## v0.8.0 (2024-08-27)

### Build

* build: remove `sphinx` from package dev dependencies ([`41f61a9`](https://github.com/xability/py_maidr/commit/41f61a915d9b3dea27419d984c8cd9408de794d5))

* build: move `black` formatter to `dev` dependencies ([`ca460b4`](https://github.com/xability/py_maidr/commit/ca460b4cca26418bee3cab2ce4949b96d5e60147))

### Feature

* feat: pick up seaborn heatmap fmt towards maidr (#90) ([`fb5dde0`](https://github.com/xability/py_maidr/commit/fb5dde0c7b2d65f6649342ff5474f032e4e36bae))

### Unknown

* chore: update `poetry.lock` ([`ac89fd7`](https://github.com/xability/py_maidr/commit/ac89fd78d5df129caeef3c57518463a6812cf4fb))

* chore: hide `chore` and `ci` updates from future release notes ([`e886067`](https://github.com/xability/py_maidr/commit/e88606736a9b9a481b5aa463e7231ca83f63521f))

* chore: clean up messy CHANGELOG ([`20785a8`](https://github.com/xability/py_maidr/commit/20785a8b95ff17132c900dc96035814d34821974))

## v0.7.0 (2024-08-24)

### Feature

* feat(maidr.show): support py-shiny renderer (#67) ([`a944826`](https://github.com/xability/py_maidr/commit/a9448263f413246213bfc2bedf8d859b3cf74695))

### Unknown

* ci: rectify commit-lint job crash (#92)

&lt;!-- Suggested PR Title: [feat/fix/refactor/perf/test/ci/docs/chore]
brief description of the change --&gt;
&lt;!-- Please follow Conventional Commits:
https://www.conventionalcommits.org/en/v1.0.0/ --&gt;

## Description

This PR resolves an issue related to the `commit-lint` job in
`.github/workflows/ci.yml`.

Closes [#91]

## Type of Change

- [X] Bug fix
- [ ] New feature
- [ ] Breaking change (fix or feature that would cause existing
functionality to not work as expected)
- [ ] Documentation update

## Checklist

- [X] My code follows the style guidelines of this project
- [X] I have performed a self-review of my code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [X] My changes generate no new warnings
- [ ] Any dependent changes have been merged and published in downstream
modules

# Pull Request

## Description
This PR addresses an issue where `commit-lint` job crashes when
validating pull requests.

## Changes Made
Currently, the commitlint config file is getting loaded as an ES module
whilst it contains vanilla javascript configurations. This causes the
job to crash because it expects a common javascript config but finds an
ES module config. To address this issue The commit-lint config file has
been changed to a `common-js` file instead of a `js` file and the
conventional commit dependancy will now be installed during the job via
npm.

## Screenshots (if applicable)
After making the changes, I tested the commit-lint job locally and here
is an excerpt of the execution:
```
(py-maidr) ➜  py_maidr git:(Krishna/fix-commitlint) act -j commit-lint -W .github/workflows/ci.yml --container-architecture linux/amd64

INFO[0000] Using docker host &#39;unix:///var/run/docker.sock&#39;, and daemon socket &#39;unix:///var/run/docker.sock&#39; 
[CI/commit-lint] 🚀  Start image=catthehacker/ubuntu:act-latest
INFO[0000] Parallel tasks (0) below minimum, setting to 1 
[CI/commit-lint]   🐳  docker pull image=catthehacker/ubuntu:act-latest platform=linux/amd64 username= forcePull=true
[CI/commit-lint] using DockerAuthConfig authentication for docker pull
INFO[0001] Parallel tasks (0) below minimum, setting to 1 
[CI/commit-lint]   🐳  docker create image=catthehacker/ubuntu:act-latest platform=linux/amd64 entrypoint=[&#34;tail&#34; &#34;-f&#34; &#34;/dev/null&#34;] cmd=[] network=&#34;host&#34;
[CI/commit-lint]   🐳  docker run image=catthehacker/ubuntu:act-latest platform=linux/amd64 entrypoint=[&#34;tail&#34; &#34;-f&#34; &#34;/dev/null&#34;] cmd=[] network=&#34;host&#34;
[CI/commit-lint]   ☁  git clone &#39;https://github.com/wagoid/commitlint-github-action&#39; # ref=v6
[CI/commit-lint] ⭐ Run Main actions/checkout@v3
[CI/commit-lint]   🐳  docker cp src=/Users/krishnaanandan/Desktop/maidr_krishna/py_maidr/. dst=/Users/krishnaanandan/Desktop/maidr_krishna/py_maidr
[CI/commit-lint]   ✅  Success - Main actions/checkout@v3
[CI/commit-lint] ⭐ Run Main Install commitlint dependencies
[CI/commit-lint]   🐳  docker exec cmd=[bash --noprofile --norc -e -o pipefail /var/run/act/workflow/1] user= workdir=
| 
| added 11 packages in 3s
| 
| 1 package is looking for funding
|   run `npm fund` for details
[CI/commit-lint]   ✅  Success - Main Install commitlint dependencies
[CI/commit-lint] ⭐ Run Main Lint commit messages
[CI/commit-lint]   🐳  docker pull image=wagoid/commitlint-github-action:6.1.1 platform=linux/amd64 username= forcePull=true
[CI/commit-lint] using DockerAuthConfig authentication for docker pull
[CI/commit-lint]   🐳  docker create image=wagoid/commitlint-github-action:6.1.1 platform=linux/amd64 entrypoint=[] cmd=[] network=&#34;container:act-CI-commit-lint-6b355268bbbb8e27234c3c935b66fc686b070544b9a3b02b47d79688837a12ff&#34;
[CI/commit-lint]   🐳  docker run image=wagoid/commitlint-github-action:6.1.1 platform=linux/amd64 entrypoint=[] cmd=[] network=&#34;container:act-CI-commit-lint-6b355268bbbb8e27234c3c935b66fc686b070544b9a3b02b47d79688837a12ff&#34;
| Lint free! 🎉
[CI/commit-lint]   ✅  Success - Main Lint commit messages
[CI/commit-lint]   ⚙  ::set-output:: results=[]
[CI/commit-lint] Cleaning up container for job commit-lint
[CI/commit-lint] 🏁  Job succeeded
(py-maidr) ➜  py_maidr git:(Krishna/fix-commitlint)
```

## Checklist
&lt;!-- Please select all applicable options. --&gt;
&lt;!-- To select your options, please put an &#39;x&#39; in the all boxes that
apply. --&gt;

- [X] I have read the [Contributor Guidelines](../CONTRIBUTING.md).
- [X] I have performed a self-review of my own code and ensured it
follows the project&#39;s coding standards.
- [X] I have tested the changes locally following
`ManualTestingProcess.md`, and all tests related to this pull request
pass.
- [ ] I have commented my code, particularly in hard-to-understand
areas.
- [ ] I have updated the documentation, if applicable.
- [ ] I have added appropriate unit tests, if applicable. ([`ae50904`](https://github.com/xability/py_maidr/commit/ae509047d6063e2cebc291c94b72281f00fa3617))

* ci(commitlint): disable commitlint line length and total length checking (#87)

closes #86 ([`3f718a7`](https://github.com/xability/py_maidr/commit/3f718a7dd12c9569ef63c9318d120d00650b5995))

## v0.6.0 (2024-08-21)

### Feature

* feat: support interactivity within ipython and quarto (#64) ([`620ddc9`](https://github.com/xability/py_maidr/commit/620ddc9d57175d5ca663d9dfaef4d2704809462f))

### Unknown

* chore: add bug report and feature request templates (#81)

Added bug report and feature request templates to improve the issue creation process. These templates provide a standardized structure for reporting bugs and requesting new features, making it easier for contributors to provide clear and concise information. This will help streamline the issue triage and resolution process.

The bug report template includes sections for describing the bug, steps to reproduce, actual and expected behavior, screenshots, and additional information. The feature request template includes sections for describing the requested feature, motivation, proposed solution, and additional context.

This commit follows the established commit message convention of starting with a verb in the imperative form, followed by a brief description of the change. It also includes a type prefix (&#34;feat&#34;) to indicate that it is a new feature.

closes #80 ([`5af72c2`](https://github.com/xability/py_maidr/commit/5af72c2cc1f01f4b1b1d1ac1944ed06c789891d8))

* chore(vscode): update shiny extension ([`483a075`](https://github.com/xability/py_maidr/commit/483a0758a68960de0670e36c312cfbc1ee90c110))

* ci: add repo name condidtion to docs workflow (#75) ([`0fb17e9`](https://github.com/xability/py_maidr/commit/0fb17e9c86d92d29b315dd3af254ae187a853abb))

## v0.5.1 (2024-08-14)

### Fix

* fix: update poetry.lock (#74) ([`6216959`](https://github.com/xability/py_maidr/commit/621695940075fe195b0310c544c117bdc5a9d35e))

### Unknown

* ci: remove poetry.lock (#73) ([`da1cd26`](https://github.com/xability/py_maidr/commit/da1cd26d8db10aabfe989a760e8df9a62a4bfe3a))

* ci: fixate python version in docs action (#71) (#72) ([`513780d`](https://github.com/xability/py_maidr/commit/513780d732ea2feb3890ace6c7028ebf5f193b17))

* ci: fixate python version in docs action (#71) ([`c0f981a`](https://github.com/xability/py_maidr/commit/c0f981a1d3741709c929af1d8616b39313501c62))

* ci: update poetry.lock (#70) ([`87ffb06`](https://github.com/xability/py_maidr/commit/87ffb06d49f4062a35f5ebee0fa0e28265ceeec5))

* chore(vscode): update settings to use numpy docstring ([`e9b0c4d`](https://github.com/xability/py_maidr/commit/e9b0c4d08eacdb4d9e40e46ffd74e13799da42d7))

* ci: upgrade quartodoc version (#62) ([`36fe34f`](https://github.com/xability/py_maidr/commit/36fe34fe52abca4be8e2101a10b76d887cd17bf2))

## v0.5.0 (2024-07-25)

### Feature

* feat: support hightlighing except for segmented plots and boxplots (#59) ([`c2cb99d`](https://github.com/xability/py_maidr/commit/c2cb99d8d7668b177dcf8b800b137eb994c85d6f))

## v0.4.2 (2024-07-02)

### Fix

* fix: seaborn multi plots in same session (#58) ([`c32fdfd`](https://github.com/xability/py_maidr/commit/c32fdfd32473dd354d292d33a19610a4c0a2eb63))

## v0.4.1 (2024-06-25)

### Fix

* fix(boxplot): support seaborn axes flip (#56) ([`023907f`](https://github.com/xability/py_maidr/commit/023907fd2482631c42803c7504bf9b838fb035c6))

## v0.4.0 (2024-06-16)

### Feature

* feat(boxplot): support horizontal orientation (#52) ([`aebfd89`](https://github.com/xability/py_maidr/commit/aebfd89d90c5d64432425745186b1fe9cceab49d))

### Fix

* fix(example): take out unused param from seaborn barplot example ([`a58001d`](https://github.com/xability/py_maidr/commit/a58001d06f19756ac9a625257301482a75c9dc6e))

## v0.3.0 (2024-06-11)

### Breaking

* feat!: support syntaxless-api (#47) ([`415d6f1`](https://github.com/xability/py_maidr/commit/415d6f1c2c9bf3f62b29da1dd752cb34a18168a3))

### Fix

* fix: black formatting ci (#49) ([`20c4fa2`](https://github.com/xability/py_maidr/commit/20c4fa231bd5a78679cce7698d2a42077c97f330))

* fix: remove docs (#48) ([`9b8cae5`](https://github.com/xability/py_maidr/commit/9b8cae5c1e4071be6edbfdbab8f4b498516f9caf))

### Unknown

* chore(deps-dev): bump black from 23.3.0 to 24.3.0 (#45)

Bumps [black](https://github.com/psf/black) from 23.3.0 to 24.3.0.
- [Release notes](https://github.com/psf/black/releases)
- [Changelog](https://github.com/psf/black/blob/main/CHANGES.md)
- [Commits](https://github.com/psf/black/compare/23.3.0...24.3.0)

---
updated-dependencies:
- dependency-name: black
  dependency-type: direct:development
...

Signed-off-by: dependabot[bot] &lt;support@github.com&gt;
Co-authored-by: dependabot[bot] &lt;49699333+dependabot[bot]@users.noreply.github.com&gt; ([`53818c9`](https://github.com/xability/py_maidr/commit/53818c9478301376461e64d1cf5a5d32ef730df2))

* ci: add workflow for publishing docs (#44)

`docs.yml` automates the publishing of py-maidr documentation to GitHub Pages. This builds the
static sources using `quarto` for the website and `quartodoc` for the API Reference.
The rendering and publishing are accomplished using Quarto&#39;s github actions, which can be found
at https://github.com/quarto-dev/quarto-actions.

Resolves: #43 ([`a6c5886`](https://github.com/xability/py_maidr/commit/a6c5886cc66339eabdfac3c8dc8bb10ee2c037c6))

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

* feat(boxplot): support matplotlib library (#32) ([`060ccfd`](https://github.com/xability/py_maidr/commit/060ccfda80bb168df00c78354b543dbd72c24f1b))

### Unknown

* ci: setup release pipeline (#42)

`release.yml` configures the github workflow to lint the commit message, format of the code, 
and the unit tests. After successfully completing those jobs, the pipeline builds the package,
updates the semantic version according to the commit message and publishes to the GitHub
Release as well as to the PyPi.

Resolves: #41 ([`634f91c`](https://github.com/xability/py_maidr/commit/634f91cdf5a806f2b451727ccc94b970c7af6a90))

* ci: setup pr github workflow (#40)

Combined the black, commit-message-lint, and the unit test workflow into one called ci.yml. This is beneficial because it could be reused in the release pipeline.

Resolves: #39 ([`4ea4bb6`](https://github.com/xability/py_maidr/commit/4ea4bb6de14854dec9234dc36938d24ed04e9902))

## v0.1.2 (2024-05-13)

### Documentation

* docs(readme): add logo ([`8702ce5`](https://github.com/xability/py_maidr/commit/8702ce5b9097fcec2a856129841d17c73e5c4415))

* docs(heatmap): add matplotlib example (#25) ([`7cb9433`](https://github.com/xability/py_maidr/commit/7cb9433ad6908a0a882bf7e7897914e1d2479a48))

* docs(readme): update base URL ([`6463477`](https://github.com/xability/py_maidr/commit/6463477cff6458d77c4bad3dc5b683cf52ee958b))

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

* feat(scatter): support matplotlib and seaborn library (#30) ([`d2d1202`](https://github.com/xability/py_maidr/commit/d2d12028350deec664614dac462f83d4e362a139))

* feat(boxplot): support seaborn library (#29) ([`5506242`](https://github.com/xability/py_maidr/commit/55062427a2f363be9eeba5abe58725a7f55aa99e))

* feat(stacked): support maidr for matplotlib and seaborn (#28) ([`9e95186`](https://github.com/xability/py_maidr/commit/9e951865b444ba3bbb932d7b8fd7b06885df0f2b))

* feat: support seaborn bar and count plot (#12) ([`fd622bd`](https://github.com/xability/py_maidr/commit/fd622bdd51236627cd37babf9e20ef1378311ff7))

* feat: redesign python binder (#10)

* feat: redesign python binder

* docs: add example bar plot ([`2fe4901`](https://github.com/xability/py_maidr/commit/2fe490158c7cba8fb40d939a079e4c0817ed349a))

### Fix

* fix: support seaborn breaking changes (#31) ([`afe5382`](https://github.com/xability/py_maidr/commit/afe538209e313f7a42c355c7234ba5f1d1ebf97b))

* fix(version): start from 0.0.1 ([`6bf23bb`](https://github.com/xability/py_maidr/commit/6bf23bb3bff2056f7b1b8d54abc1539d666269ae))

* fix: update pyproject.toml version and htmltools dependency (#14) ([`fcaca48`](https://github.com/xability/py_maidr/commit/fcaca486dff79ac6861d9561986088f432d74b64))

### Test

* test(barplot): add unit tests for barplot (#20)

* test(barplot): add unit tests for barplot

* chore: add mocks for inputs

* test: add common fixtures

* chore: correct test input

* test: add unit tests for bar plot

* test: add tox workflow

* test: add correct python version

* test: remove non-deterministic assert comment ([`af81cd9`](https://github.com/xability/py_maidr/commit/af81cd935a5bfc1f76c43e4ed16665d11c383605))

### Unknown

* ci: update version to 0.1.1 (#27) ([`4ceff90`](https://github.com/xability/py_maidr/commit/4ceff90c6841e4d08fa1b3316a2ee6be75e50f92))

* feat/heatmap, lineplot, histogram (#24) ([`5914f07`](https://github.com/xability/py_maidr/commit/5914f07a5a4eb2687af585df1d0f2c6ca7974038))

* chore/change to manual publishing (#23) ([`1bc6307`](https://github.com/xability/py_maidr/commit/1bc63077eac20970964d1c68c8a88bafdc4133a4))

* chore: update project homepage URL ([`2aeb15c`](https://github.com/xability/py_maidr/commit/2aeb15c4625aface3db289d6e7634ed30516bb58))

* chore: add homepage URL to pyproject.toml ([`582a23f`](https://github.com/xability/py_maidr/commit/582a23f4bb98327edac8b8ae2ed60a59bbf6e3e4))

* chore: update pyproject.toml with additional metadata ([`314cd38`](https://github.com/xability/py_maidr/commit/314cd386d2f6a4ecaa5635dd433bd68e9b67fe9b))

* chore(vscode): add GitLens extension ([`3491ecc`](https://github.com/xability/py_maidr/commit/3491ecc6e5f7ade3fc9fe78d2d31e7616a41215e))

* chore(vscode): remove brackets from the title ([`99ecd10`](https://github.com/xability/py_maidr/commit/99ecd10d4e7b19b05a22fd21276b5fcb54406e6a))

* Merge branch &#39;main&#39; of https://github.com/uiuc-ischool-accessible-computing-lab/py_maidr ([`9e16c28`](https://github.com/xability/py_maidr/commit/9e16c288bb72b17ff8076caa324c80649a583516))

* chore(vscode): add git.ignoreRebaseWarning setting to .vscode/settings.json ([`97c27a8`](https://github.com/xability/py_maidr/commit/97c27a8c694b3c84870a82bfb60d9ae05c6cbec2))

* chore(vscode): add ms-python.debugpy extension to extensions.json ([`ac1b619`](https://github.com/xability/py_maidr/commit/ac1b61957db84631f6616787d404e4053ec5ab26))

* chore(vscode): update window title in VS Code settings.json ([`065800e`](https://github.com/xability/py_maidr/commit/065800ede282c861678c71b0a3e258a6e2bd496f))

* ci: :wrench: fix commmit linter gh action to be triggered against the latest commit only ([`dbb86d3`](https://github.com/xability/py_maidr/commit/dbb86d38e48e7f44908b61fab1d3122b09ce8bfc))

* ci: :wrench: fix commmit linter gh action to be triggered against the latest commit only ([`f53251c`](https://github.com/xability/py_maidr/commit/f53251c5510901b51b7f615e49f565bc0a9bf351))

* ci: add conventional commits linter to gh workflowFixes #5

* ci: add conventional commits linter to gh workflow
Fixes #5 ([`f1babab`](https://github.com/xability/py_maidr/commit/f1babab54ba44f211657386be17e839523c5c92f))

* ci: :wrench: add python-semantic-release dependencies and settings ([`f928eff`](https://github.com/xability/py_maidr/commit/f928eff5e923a5130b3cfbdb45d93ae9b2174346))

* ci: :sparkles: add conventional commits linter to gh action ([`fc4b758`](https://github.com/xability/py_maidr/commit/fc4b758fb9b9ebd84dc83c9d4423bb3bdc6f4940))

* chore(.vscode): add conventional commits extensions ([`492d23f`](https://github.com/xability/py_maidr/commit/492d23ff70803ab2c82e71fee487c019ee743dd1))

* chore(.vscode): :wrench: add conventional commits settings ([`7cb39cd`](https://github.com/xability/py_maidr/commit/7cb39cd1af091eecc35f448fbe20ff610f7ed7c8))

* chore(.vscode): :wrench: add conventional commits settings ([`e8e782f`](https://github.com/xability/py_maidr/commit/e8e782f198cba310494ef817e71bddd0374ce58a))

* chore: use copilot to describe pr ([`5bc8803`](https://github.com/xability/py_maidr/commit/5bc8803684eaaf17c34301b08a677a5b02bc505e))

* chore: remove spellright extension ([`85b7bdf`](https://github.com/xability/py_maidr/commit/85b7bdf590c9ed6a6b9588e6e33d22f502848bd1))

* update README ([`c16a378`](https://github.com/xability/py_maidr/commit/c16a37821225656a86804ac555f723ba00987a5d))

* chore: add more vscode settings and extensions ([`0bf19ba`](https://github.com/xability/py_maidr/commit/0bf19ba68094f46d08af7297a4c93c0e5215ad62))

* Add Python REPL smart send and activate
environment in terminal ([`7321428`](https://github.com/xability/py_maidr/commit/732142855f1ddc8948f53d6d562b5c202e028c44))

* remove html file ([`874d1b7`](https://github.com/xability/py_maidr/commit/874d1b7d2026855eb50b0c974d88d8c03faf60cb))

* Update dependencies in poetry.lock and
pyproject.toml ([`de9f113`](https://github.com/xability/py_maidr/commit/de9f11336582af8df0ca02f11d06c541fef027f6))

* Remove Flake8 linting and update formatting
settings ([`94da4f3`](https://github.com/xability/py_maidr/commit/94da4f3c1ba82f088b343b0d758432504e014baf))

* add .conda to .gitignore ([`08b50f9`](https://github.com/xability/py_maidr/commit/08b50f9be1e311c599a94634dd3a6e7f0bda5da7))

* fixed text display bug ([`616bd26`](https://github.com/xability/py_maidr/commit/616bd26140be8435b8fad90b60b9ad740c2d9807))

* updated js with working code ([`23911e9`](https://github.com/xability/py_maidr/commit/23911e9976526fcbf3a9113bd803f5d3f37fd3ff))

* [tobeRemoved] html file generated for barplot using maidr ([`13340cc`](https://github.com/xability/py_maidr/commit/13340cc61e80c5190e1739c8ba471d14cd86021d))

* [WIP] integration of maidr with a.[done] barplot and countplot .[WIP] scatterplot c.[WIP] heatmap ([`3c21f88`](https://github.com/xability/py_maidr/commit/3c21f880ea3652b121fe88a7b2f82036eb51f1b7))

* add example ([`86d104a`](https://github.com/xability/py_maidr/commit/86d104aff56fc493e7533b9089ac31475d70c45e))

* add a more description on poetry run to README ([`3cac3c4`](https://github.com/xability/py_maidr/commit/3cac3c45f99693a6fea3c940f27ff2d0209bd13b))

* deleted layer_data and chart.html ([`a5af285`](https://github.com/xability/py_maidr/commit/a5af285057825c287d6ddd8260a7f92149707b8a))

* sonification of heat map ([`d2615d6`](https://github.com/xability/py_maidr/commit/d2615d6436ef59bbebaff692a4ef607e8ceb9a4a))

* Merge branch &#39;main&#39; of https://github.com/uiuc-ischool-accessible-computing-lab/py-maidr into main ([`19f6a49`](https://github.com/xability/py_maidr/commit/19f6a49195fd9166abf3785bbd1934f02ff5efd1))

* change module name: c2m -&gt; maidr ([`2911628`](https://github.com/xability/py_maidr/commit/2911628f8e0460cd887b27efd1fc94141ad36504))

* [WIP] boxplot data extraction ([`bbbcce0`](https://github.com/xability/py_maidr/commit/bbbcce0347f025366a3a1f412a90369903637bec))

* [InProgress] heatmap visual sync ([`2738d92`](https://github.com/xability/py_maidr/commit/2738d924df4425f0871b09e5fbe0a35d0e066332))

* Revert &#34;WIP: restructure package src&#34;

This reverts commit d8206b0c64a0c5b6e21e33d75382f271b19b8858. ([`590b81a`](https://github.com/xability/py_maidr/commit/590b81a44143d4000cfdbf6e75cf458ba7c0bd94))

* WIP: restructure package src ([`d8206b0`](https://github.com/xability/py_maidr/commit/d8206b0c64a0c5b6e21e33d75382f271b19b8858))

* add pytest dependency ([`ba903d5`](https://github.com/xability/py_maidr/commit/ba903d55e5ef0600c3d83c4e4eac7fa657db204e))

* update README ([`ba7b4b9`](https://github.com/xability/py_maidr/commit/ba7b4b96d710929f4c99d0d1bcf12bbd7516c80a))

* add pre-commit dependency ([`215e60d`](https://github.com/xability/py_maidr/commit/215e60dc6c15cf9b4fa74f57235150234cc9b15e))

* organize package structure ([`b3698ef`](https://github.com/xability/py_maidr/commit/b3698ef1344d3885b5aab2e6a9727dd5ddf14f28))

* add .gitignore ([`94c44cd`](https://github.com/xability/py_maidr/commit/94c44cd437c841757abbb21bc790568f8c933264))

* scatterplot: use a list comprehension instead of a for loop ([`8aea0b2`](https://github.com/xability/py_maidr/commit/8aea0b22708af57baad68d358f425fcde4ea7f88))

* lineplot: use a list comprehension instead of a for loop ([`fd6b725`](https://github.com/xability/py_maidr/commit/fd6b725e2455c9ed1366ef8948b2cf4ec885abf4))

* countplot: use list comprehension instead of for loop ([`de2b209`](https://github.com/xability/py_maidr/commit/de2b2093d94608db53acc408941d19e44b28843a))

* VSCode: more settings ([`86aaf7c`](https://github.com/xability/py_maidr/commit/86aaf7cdaec3ce1161370009cfc29039e843f462))

* adding chart.html ([`ac5394b`](https://github.com/xability/py_maidr/commit/ac5394b4b1d7a5f7ee55c4e9df3c19e3d05b093c))

* [InProgress] heatmap sonification ([`3506b77`](https://github.com/xability/py_maidr/commit/3506b77e4e767025a8bb1232191aa73d34cb4ef1))

* fix html template to accept x and y labels ([`bf2e0ff`](https://github.com/xability/py_maidr/commit/bf2e0ff5994d54562f8847931213b687d19cd1d0))

* delete html ([`a62db10`](https://github.com/xability/py_maidr/commit/a62db1092fafea704bbdccce14add6a0ffb5e340))

* fix x tick bug in html template ([`ef038da`](https://github.com/xability/py_maidr/commit/ef038daeb84a45fdbb06459f46b70efb6dc8984d))

* use a unique id per plot element ([`53e22b3`](https://github.com/xability/py_maidr/commit/53e22b33c8e8bea40eaf5af8ea30163eb4ded13a))

* Merge branch &#39;main&#39; of https://github.com/uiuc-ischool-accessible-computing-lab/py-maidr ([`d85366c`](https://github.com/xability/py_maidr/commit/d85366c98b417a57d22b83069b2078ab2988d16d))

* [InProgress] Partial sonification of heatmap ([`a3b771c`](https://github.com/xability/py_maidr/commit/a3b771c6c953731249fa5fa207d41ebad1701d6e))

* refactor c2m module ([`68e1016`](https://github.com/xability/py_maidr/commit/68e101612df87d79fa53df46e48cb52d953d4324))

* WIP: c2m module ([`6785205`](https://github.com/xability/py_maidr/commit/678520506faa9a78eb23a2bf22d33f17dec2ce22))

* Merge pull request #3 from uiuc-ischool-accessible-computing-lab/c2m

fix #1: start c2m module ([`205ea3f`](https://github.com/xability/py_maidr/commit/205ea3f1158c1b1bde8988b3ecc86783822df2f7))

* start c2m module ([`a1453e1`](https://github.com/xability/py_maidr/commit/a1453e1edbcb182378bfb195c6f039b8bf0152c2))

* Merge branch &#39;main&#39; of https://github.com/uiuc-ischool-accessible-computing-lab/py-maidr into main ([`e759ab8`](https://github.com/xability/py_maidr/commit/e759ab8c76964ab57c56df85bd9cb571e5102822))

* VSCode: add more settings and extensions ([`70a6f7c`](https://github.com/xability/py_maidr/commit/70a6f7cba3ec728fd4e91fb861879fb1e87329d5))

* [InProgress] heatmap data extraction ([`4b19490`](https://github.com/xability/py_maidr/commit/4b19490620e494ec6e546494b47fa95a12d0ed8d))

* update readme ([`2ce3a5a`](https://github.com/xability/py_maidr/commit/2ce3a5a8f2bb8f5a8c49f658234f3ec333bad074))

* VSCode setting: always show black format notification ([`a0d84f8`](https://github.com/xability/py_maidr/commit/a0d84f8ee78493b6e40eba4a7024a5726796f08e))

* add isort settings ([`4547df1`](https://github.com/xability/py_maidr/commit/4547df1e7c14981f2b31a225d68f9c471672cd34))

* add flake8 linter setting ([`d738f5b`](https://github.com/xability/py_maidr/commit/d738f5b909c49ba8cc939f7945450ffca5b4b815))

* fix lint ([`6870273`](https://github.com/xability/py_maidr/commit/68702737f9c0ebf1d742b43e8a3dde52a4e93088))

* test formatting ([`b58932a`](https://github.com/xability/py_maidr/commit/b58932a68bf19be4c4b9db7088dae650a55d46ea))

* fix indent ([`f0398b9`](https://github.com/xability/py_maidr/commit/f0398b947f3bbb335473772dd74e492e03a25249))

* fix GH action: black formatter ([`7ce9de2`](https://github.com/xability/py_maidr/commit/7ce9de2ce125dc4b637b1c56d2ba792dd8e4da42))

* test format ([`42f79fa`](https://github.com/xability/py_maidr/commit/42f79fa5d606b0b945ce15383ae008bff02ab308))

* add GH action to auto-format code using black ([`e421dfc`](https://github.com/xability/py_maidr/commit/e421dfcdfc1fb5486332aba519221173bd0826d9))

* add instruction for pre-commit to readme ([`a967ac7`](https://github.com/xability/py_maidr/commit/a967ac7fcfd9a21fd187019b63f3a8861662c76a))

* resolve conflict ([`15de2c9`](https://github.com/xability/py_maidr/commit/15de2c9535d74f62ab03a23bf2b3b236240c4ceb))

* add  to pre-commit ([`7bba7bd`](https://github.com/xability/py_maidr/commit/7bba7bd3016db9ec46217e7a6821ac19dfe6acc1))

* add black to pre-commit ([`377312d`](https://github.com/xability/py_maidr/commit/377312df854d60f44c01bf86b8b2673eb0a8538a))

* add VSCode settings and extensions ([`7b36507`](https://github.com/xability/py_maidr/commit/7b365079d0c9aefbf805811dc1fe4e39656473f2))

* Merge branch &#39;master&#39; ([`ddba335`](https://github.com/xability/py_maidr/commit/ddba3353d45cf83d6748fd0a2f4703888a635e36))

* [in progress] sonification for line chart ([`d4466bc`](https://github.com/xability/py_maidr/commit/d4466bcdc86abd39f6c9af3ac4b20d8518196cce))

* sonification for scatter plot ([`4c92bf4`](https://github.com/xability/py_maidr/commit/4c92bf47272af6f6348a8eb7b4587367605107cb))

* sonification for count plot ([`816f4bc`](https://github.com/xability/py_maidr/commit/816f4bc7f8cbeeb0e4023f66eabe5a9c2540e3e1))

* sonification of bar chart ([`b820ac8`](https://github.com/xability/py_maidr/commit/b820ac80467fbdfff4a4a4dedf7aae8af0b9b029))

* updated files to support dynamic data passing to html template ([`7cf4eec`](https://github.com/xability/py_maidr/commit/7cf4eec9c5db2ddbe589213adbefee1ca51b0f12))

* Integrate chart2music for bar plot ([`3484cbe`](https://github.com/xability/py_maidr/commit/3484cbe96febc90375cb4faba31bdd0df5866128))

* a.refactored code b.added json option ([`860a164`](https://github.com/xability/py_maidr/commit/860a16414053160cf30602be576f17ff653b8bfe))

* removed plt.show ([`61a3a33`](https://github.com/xability/py_maidr/commit/61a3a33bb184994c5d8f4b13caa771c7cefd277c))

* single lineplot ([`cc626f8`](https://github.com/xability/py_maidr/commit/cc626f88b475a8cbb288225b564d30537eab3fb1))

* bar plot and scatter plot ([`1329412`](https://github.com/xability/py_maidr/commit/1329412ee9b7a4c21b5b5faabc754aef1f5f73a2))

* function for countplot ([`1e63690`](https://github.com/xability/py_maidr/commit/1e63690cf35c2587dcba307d2eb1884ea62f0c69))

* initial commit ([`ec22a67`](https://github.com/xability/py_maidr/commit/ec22a6769151a47ddfebd1ded0ba69c76f89f0bf))

* Initial commit ([`673f1e9`](https://github.com/xability/py_maidr/commit/673f1e91b0fb40bf407b841d939ffbb1af5feb61))
