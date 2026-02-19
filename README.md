# Python Practice Portfolio

A curated collection of Python exercises and notebooks from the **CS50 Programming with Python** track, organized by topic and used to practice core software engineering fundamentals.

This repository is intentionally structured as a learning portfolio rather than a production application. It demonstrates problem-solving progression across language fundamentals, testing, object-oriented programming, and practical tooling.

## Why this repository exists

This project showcases:

- **Foundational Python fluency** (conditionals, loops, exceptions, functions).
- **Applied programming skills** (libraries, HTTP requests, regex, file I/O).
- **Testing awareness** with unit-test examples using `pytest`.
- **Object-oriented design practice** including classes, inheritance, and special methods.
- **Consistent iteration** through lecture-based, incremental examples.

For interviewers and product stakeholders, this repository represents a transparent learning journey, with code artifacts that make growth and technical reasoning easy to inspect.

## Repository structure

```text
python-prac/
├── CS-50-Programming-with-python/
│   ├── Lecture 1 - Conditionals.ipynb
│   ├── Lecture 2 - Loops.ipynb
│   ├── Lecture 3 - Exceptions.ipynb
│   ├── Lecture 4 - Libraries.ipynb
│   ├── Lecture 5 - Unit Tests/
│   │   ├── Calculator.py
│   │   ├── test_calculator.py
│   │   └── pytest_executor.ipynb
│   ├── Lecture 6 - File IO/
│   ├── Lecture 7 - Regular Expressions.ipynb
│   ├── Lecture 8 - OOP/
│   └── Lecture 9 - Et Cetera/
└── .github/workflows/ci.yml
```

## Highlights

- **Notebook-first learning format:** Most examples are in Jupyter notebooks for fast experimentation and concept exploration.
- **Tested Python module example:** `Calculator.py` and `test_calculator.py` demonstrate a minimal unit testing workflow.
- **CI sanity check:** A GitHub Actions workflow runs `python -m compileall .` on pull requests to catch syntax issues early.

## How to explore this repo

1. Start with lectures in numerical order to follow concept progression.
2. Open notebooks in Jupyter or VS Code.
3. Review `Lecture 5 - Unit Tests` for standalone Python files and `pytest` usage.
4. Use examples as templates for your own practice extensions.

## Local setup

### Prerequisites

- Python 3.10+
- `pip`
- (Optional) Jupyter Notebook or VS Code with Jupyter extension

### Install dependencies

This repo is lightweight and mostly standard-library based. For test execution:

```bash
pip install pytest
```

### Run checks

```bash
python -m compileall .
```

```bash
pytest "CS-50-Programming-with-python/Lecture 5 - Unit Tests/test_calculator.py" -v
```

## Suggested next improvements

- Add a `requirements.txt` to formalize tooling dependencies.
- Convert selected notebooks into reusable `.py` modules.
- Expand unit tests with broader input coverage.
- Add brief learning notes per lecture (what changed, what was learned, and what's next).

---

If you're reviewing this as an interviewer or PM, think of this repository as a practical evidence trail of iterative technical growth, not a single finished product.
