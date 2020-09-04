## Cannot Run Python from code-runner

When clicking code-runner directly, get error `/bin/sh: 1: python: not found`, but if right-clike in VSCode and choose "Run python file in terminal", it runs smoothly.

The fix is through setting `code-runner.executorMap`, as below:

Original: `Python: python -u`

Change to: `Python: python3 -u`
