# Continuous Integration example for Python


### To get started
* Create an empty virtual environment
`conda create -n test_env python=3.5`
  * Activate it and populate it with the minimal tools to run the tests, for this example, install `pandas`
  * Generate a requirements.txt using:
`pip freeze > requirements.txt`
* Create a `.travis.yml` file in the root of the repository.  It should have at least the following sections:
```
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
