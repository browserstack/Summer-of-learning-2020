# The Basics: Getting started with Selenium

If you’re starting out with test automation or Selenium, this is a great episode for you. You’ll learn what Selenium is, how you can set up and write your first test, what to look for in frameworks, and how to pick the best framework for you.

Speakers: [David Burns](https://github.com/automatedtester)
          Charlie Lee

## How to run the tests

These tests are written in python. You will need to install python if you are on a machine with Windows. 

### Install dependencies

Run the following command. This will make sure the python dependencies to run the tests are setup.

```bash
pip install -r requirements.txt
```

You will need to download the relevant driver executables from each of the browser vendors. Below are links to each of them:
* [geckodriver](https://github.com/mozilla/geckodriver/releases)
* [chromedriver](https://sites.google.com/a/chromium.org/chromedriver/)

Place them in the same directory and then add that directory to the environment variable `PATH`. E.g.
```bash

export PATH=/path/to/driver/binarys:$PATH

```
