# Contributing

Keep each change tied to a numbered book exercise. A solution should be readable by someone who has reached that chapter, use only the Python standard library and include a focused `unittest` check.

Before opening a change, run:

```bash
python -m unittest discover -s chapters -t . -p "test_*.py"
python tools/check_repository.py
```

Do not commit the Word manuscript, generated output or local virtual environments.
