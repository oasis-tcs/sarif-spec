# Notes on tools

Before committing changes to the python files in here, please ensure the following commands succeed:

  + mypy $FILE (for type verification)
  + ruff --ignore E501 $FILE (for general linting)
  + black -S -l120 $FILE (for 120 lines and single quotes preferred format)
  + vale --config $FILE (developer documentation spell check)
