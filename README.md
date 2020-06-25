# go-test

## Description

ci plugin to run go test, upload coverage percentage and report

## Inputs

- `WITH_GO_CACHE`: enable or disable go cache, default value is `false` for disalbe

## How to use it

```yml
#  Example that togeher with git clone plugin

envs:
  FLOWCI_GIT_URL: "https://github.com/gin-gonic/gin.git"
  FLOWCI_GIT_BRANCH: "master"

steps:
  - name: clone
    plugin: 'gitclone'
    allow_failure: false

  - name: test
    plugin: go-test
```

## Screenshot

#### Coverage report

![](https://raw.githubusercontent.com/gy2006/flowci-plugin-go-test/master/resources/coverage-report.png)