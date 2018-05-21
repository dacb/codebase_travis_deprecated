# Continuous Integration example for Python

[![Build Status](https://travis-ci.org/dacb/codebase.svg?branch=master)](https://travis-ci.org/dacb/codebase)
[![Coverage Status](https://coveralls.io/repos/github/dacb/codebase/badge.svg?branch=master)](https://coveralls.io/github/dacb/codebase?branch=master)

### To get started
* Go to https://travis-ci.org/ and sign using your GitHub account.  Click on the _+_ button next to the list of repositories on the left hand side. Select the repo from the list and enable the service by flipping the slider.
* Create an empty virtual environment
`conda create -n test_env python=3.5`
  * Activate it and populate it with the minimal tools to run the tests, for this example:
```
source activate test_env
conda install pip
pip install pandas
```
  * Generate a requirements.txt using:
`pip freeze > requirements.txt`
* Create a `.travis.yml` file in the root of the repository.  It should have at least the following sections:
```
# what language the build will be configured for
language: python

# specify what versions of python will be used
# note that all of the versions listed will be tried
python:
    - 3.4
    - 3.5
    - 2.7
    
# what branches should be evaluated
branches:
    only:
        - master

# list of commands to run to setup the environment
install:
    - pip install coverage
    - pip install coveralls
    - pip install flake8
    - pip install -r requirements.txt


# a list of commands to run before the main script
before_script:
    - "flake8 codebase"

# the actual commands to run
script:
    - coverage run -m unittest discover

# generate a coverage report to send to back to user
after_success:
    - coverage report
    - coveralls

```
* Sometimes you need to install operating system level dependencies using `apt-get` in which case you will need to add the following lines:
```
sudo: true
```
Then you can add lines for install dependencies using `apt-get` to your `before_install` section, e.g.
```
before_install:
    - apt-get install some_os_dependency
```
* The order of build operations is:
  * `before_install`
  * `install`
  * `before_script`
  * `script`
  * `after_success` or `after_failure`
  * OPTIONAL `before_deploy`
  * OPTIONAL `deploy`
  * OPTIONAL `after_deploy`
  * `after_script`
* If any of the commands in the first four stages of the build lifecycle return a non-zero exit code, the build is broken:
  * If `before_install`, `install` or `before_script` return a non-zero exit code, the build is errored and stops immediately.
  * If `script` returns a non-zero exit code, the build is failed, but continues to run before being marked as failed.
  * The exit code of `after_success`, `after_failure`, `after_script` and subsequent stages do not affect the build result. However, if one of these stages times out, the build is marked as a failure.
* Other settings that occasionally come into play include,
  * How submodules are handled.  By default all submodules are cloned.  If this isn't what you want, you can use:
```
git:
  submodules: false
```
  * If you are using Git LFS, you will need to remember to install it and describe how it is used, e.g.
```
before_install:
		- echo -e "machine github.com\n  login $GITHUB_TOKEN" >> ~/.netrc
		- git lfs pull
```
  * Usually, you want to make sure the master branch is tested, but it may be necessary to include or exclude other branches, e.g.
```
# blocklist
branches:
    except:
      - legacy
      - experimental

# safelist
branches:
    only:
      - master
      - stable
```
* Other common items:
  * _Special note_: Note that for historical reasons .travis.yml needs to be present on all active branches of your project.
  * A build will be skipped if the following text appears in a commit message `[skip ci]`
  * When you specify multiple environment features like python versions or library versions you are creating a matrix of environments to be used for testing.  Each one will be tested separately.
* Create a `.coveragerc` file that specifies what should be included in the coverage calculations, e.g.
```
[report]
omit =  
    */python?.?/*
    */site-packages/nose/*
    *__init__*
exclude_lines =
    if __name__ == .__main__.:
```
* You can add a build status badge to your `README.md` by following these instructions: https://docs.travis-ci.com/user/status-images/
* If you used this template, you will also have coverage data that you can get a badge for.  To do that, sign in to https://coveralls.io with your GitHub account.  On the left hand side select _ADD REPOS_ and flip the slider switch for the repo you want.  Look for the box at the bottom of the page labeled _BADGE YOUR REPO: CODEBASE_ and click the _EMBED_ button to get a list of the ways to embed and copy the markdown one and paste it in your README.
* Now you are ready to go.  `add` `commit` `push` and it should trigger.
