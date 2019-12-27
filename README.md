# go-test

## Description

ci plugin to run go test and upload test report

## Inputs

- `FLOWCI_GIT_REPO` (required): git repo name  

## How to use it

```yml
#  Example that togeher with git clone plugin

envs:
  FLOWCI_GIT_URL: "https://github.com/FlowCI/spring-petclinic-sample.git"
  FLOWCI_GIT_BRANCH: "master"
  FLOWCI_GIT_REPO: "spring-petclinic"

steps:
  - name: clone
    plugin: 'gitclone'
    allow_failure: false

  - name: run unit test
    plugin: 'maven-test'
```

## Screenshot

#### Coverage report

![](https://raw.githubusercontent.com/gy2006/flowci-plugin-go-test/master/resources/coverage-report.png)