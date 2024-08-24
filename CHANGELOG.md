# CHANGELOG

## v0.7.0 (2024-08-24)

### Ci

* ci: rectify commit-lint job crash (#92)

* ci(commitlint): disable commitlint line length and total length checking (#87)

### Feature

* feat(maidr.show): support py-shiny renderer (#67) ([`a944826`](https://github.com/xability/py_maidr/commit/a9448263f413246213bfc2bedf8d859b3cf74695))

## v0.6.0 (2024-08-21)

### Chore

* chore: add bug report and feature request templates (#81)

* chore(vscode): update shiny extension ([`483a075`](https://github.com/xability/py_maidr/commit/483a0758a68960de0670e36c312cfbc1ee90c110))

### Ci

* ci: add repo name condidtion to docs workflow (#75) ([`0fb17e9`](https://github.com/xability/py_maidr/commit/0fb17e9c86d92d29b315dd3af254ae187a853abb))

### Feature

* feat: support interactivity within ipython and quarto (#64) ([`620ddc9`](https://github.com/xability/py_maidr/commit/620ddc9d57175d5ca663d9dfaef4d2704809462f))

## v0.5.1 (2024-08-14)

### Chore

* chore(vscode): update settings to use numpy docstring ([`e9b0c4d`](https://github.com/xability/py_maidr/commit/e9b0c4d08eacdb4d9e40e46ffd74e13799da42d7))

### Ci

* ci: remove poetry.lock (#73) ([`da1cd26`](https://github.com/xability/py_maidr/commit/da1cd26d8db10aabfe989a760e8df9a62a4bfe3a))

* ci: fixate python version in docs action (#71) (#72) ([`513780d`](https://github.com/xability/py_maidr/commit/513780d732ea2feb3890ace6c7028ebf5f193b17))

* ci: fixate python version in docs action (#71) ([`c0f981a`](https://github.com/xability/py_maidr/commit/c0f981a1d3741709c929af1d8616b39313501c62))

* ci: update poetry.lock (#70) ([`87ffb06`](https://github.com/xability/py_maidr/commit/87ffb06d49f4062a35f5ebee0fa0e28265ceeec5))

* ci: upgrade quartodoc version (#62) ([`36fe34f`](https://github.com/xability/py_maidr/commit/36fe34fe52abca4be8e2101a10b76d887cd17bf2))

### Fix

* fix: update poetry.lock (#74) ([`6216959`](https://github.com/xability/py_maidr/commit/621695940075fe195b0310c544c117bdc5a9d35e))

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

### Chore

* chore(deps-dev): bump black from 23.3.0 to 24.3.0 (#45)

### Ci

* ci: add workflow for publishing docs (#44)

### Fix

* fix: black formatting ci (#49) ([`20c4fa2`](https://github.com/xability/py_maidr/commit/20c4fa231bd5a78679cce7698d2a42077c97f330))

* fix: remove docs (#48) ([`9b8cae5`](https://github.com/xability/py_maidr/commit/9b8cae5c1e4071be6edbfdbab8f4b498516f9caf))

## v0.2.0 (2024-05-16)

### Ci

* ci: setup release pipeline (#42)

* ci: setup pr github workflow (#40)

### Documentation

* docs: add quarto and quartodoc for static website (#38)

* docs: add docstring (#34) ([`59f0ca1`](https://github.com/xability/py_maidr/commit/59f0ca1551643f9077fe2891af153e5038ddefe8))

### Feature

* feat: use htmltools instead of str (#33)

* feat: use htmltools instead of str

* feat: show html using htmltools

* chore: move mixin to utils package ([`8b0a838`](https://github.com/xability/py_maidr/commit/8b0a838bf7cd73ecd5e036d9be28e8ed0523a9ed))

* feat(boxplot): support matplotlib library (#32) ([`060ccfd`](https://github.com/xability/py_maidr/commit/060ccfda80bb168df00c78354b543dbd72c24f1b))

## v0.1.2 (2024-05-13)

### Chore

* chore: update project homepage URL ([`2aeb15c`](https://github.com/xability/py_maidr/commit/2aeb15c4625aface3db289d6e7634ed30516bb58))

* chore: add homepage URL to pyproject.toml ([`582a23f`](https://github.com/xability/py_maidr/commit/582a23f4bb98327edac8b8ae2ed60a59bbf6e3e4))

* chore: update pyproject.toml with additional metadata ([`314cd38`](https://github.com/xability/py_maidr/commit/314cd386d2f6a4ecaa5635dd433bd68e9b67fe9b))

* chore(vscode): add GitLens extension ([`3491ecc`](https://github.com/xability/py_maidr/commit/3491ecc6e5f7ade3fc9fe78d2d31e7616a41215e))

* chore(vscode): remove brackets from the title ([`99ecd10`](https://github.com/xability/py_maidr/commit/99ecd10d4e7b19b05a22fd21276b5fcb54406e6a))

* chore(vscode): add git.ignoreRebaseWarning setting to .vscode/settings.json ([`97c27a8`](https://github.com/xability/py_maidr/commit/97c27a8c694b3c84870a82bfb60d9ae05c6cbec2))

* chore(vscode): add ms-python.debugpy extension to extensions.json ([`ac1b619`](https://github.com/xability/py_maidr/commit/ac1b61957db84631f6616787d404e4053ec5ab26))

* chore(vscode): update window title in VS Code settings.json ([`065800e`](https://github.com/xability/py_maidr/commit/065800ede282c861678c71b0a3e258a6e2bd496f))

* chore(.vscode): add conventional commits extensions ([`492d23f`](https://github.com/xability/py_maidr/commit/492d23ff70803ab2c82e71fee487c019ee743dd1))

* chore(.vscode): :wrench: add conventional commits settings ([`7cb39cd`](https://github.com/xability/py_maidr/commit/7cb39cd1af091eecc35f448fbe20ff610f7ed7c8))

* chore(.vscode): :wrench: add conventional commits settings ([`e8e782f`](https://github.com/xability/py_maidr/commit/e8e782f198cba310494ef817e71bddd0374ce58a))

* chore: use copilot to describe pr ([`5bc8803`](https://github.com/xability/py_maidr/commit/5bc8803684eaaf17c34301b08a677a5b02bc505e))

* chore: remove spellright extension ([`85b7bdf`](https://github.com/xability/py_maidr/commit/85b7bdf590c9ed6a6b9588e6e33d22f502848bd1))

* chore: add more vscode settings and extensions ([`0bf19ba`](https://github.com/xability/py_maidr/commit/0bf19ba68094f46d08af7297a4c93c0e5215ad62))

### Ci

* ci: update version to 0.1.1 (#27) ([`4ceff90`](https://github.com/xability/py_maidr/commit/4ceff90c6841e4d08fa1b3316a2ee6be75e50f92))

* ci: :wrench: fix commmit linter gh action to be triggered against the latest commit only ([`dbb86d3`](https://github.com/xability/py_maidr/commit/dbb86d38e48e7f44908b61fab1d3122b09ce8bfc))

* ci: :wrench: fix commmit linter gh action to be triggered against the latest commit only ([`f53251c`](https://github.com/xability/py_maidr/commit/f53251c5510901b51b7f615e49f565bc0a9bf351))

* ci: add conventional commits linter to gh workflowFixes #5

* ci: add conventional commits linter to gh workflow

* ci: :wrench: add python-semantic-release dependencies and settings ([`f928eff`](https://github.com/xability/py_maidr/commit/f928eff5e923a5130b3cfbdb45d93ae9b2174346))

* ci: :sparkles: add conventional commits linter to gh action ([`fc4b758`](https://github.com/xability/py_maidr/commit/fc4b758fb9b9ebd84dc83c9d4423bb3bdc6f4940))

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
