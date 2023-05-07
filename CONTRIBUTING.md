# Contributing to Pygkit

We're glad you're interested in contributing to Pygkit! This document outlines the contribution process and guidelines to help make your experience smooth and successful.

## Table of Contents

- [Getting Started](#getting-started)
- [Pull Requests](#pull-requests)
- [Coding Standards](#coding-standards)
- [Testing](#testing)

## Getting Started

1. Fork the repository on GitHub.
2. Clone your fork to your local machine: `git clone https://github.com/yourusername/pygkit.git`
3. Add the upstream repository to your remotes: `git remote add upstream https://github.com/owner/pygkit.git`
4. Create a new branch for your feature, bug fix, or improvement: `git checkout -b my-feature-branch`

## Pull Requests

1. Make your changes, additions, or updates to the code.
2. Commit your changes with a clear and concise commit message: `git commit -m "Add feature X"`
3. Push your branch to your fork on GitHub: `git push origin my-feature-branch`
4. Create a pull request from your fork to the upstream repository.
5. Provide a clear description of your changes in the pull request and reference any related issues.

Please note that the `main` branch should always be in a stable, releasable state. Ensure your changes don't break the existing code or introduce bugs.

## Coding Standards

We follow [PEP-8](https://www.python.org/dev/peps/pep-0008/) coding style guidelines for Python. Please make sure your contributions adhere to these standards.

For documenting code, we use Google-style docstrings. Ensure your contributions follow this convention for consistency and readability. You can find more information about Google-style docstrings [here](https://google.github.io/styleguide/pyguide.html#38-comments-and-docstrings). Here's a brief example:

```python
def example_function(arg1, arg2):
    """Example function to demonstrate Google-style docstrings.

    Args:
        arg1 (int): The first argument.
        arg2 (str): The second argument.

    Returns:
        bool: True if successful, False otherwise.
    """
    # Function implementation here
```

## Testing

Before submitting your pull request, ensure your changes pass all tests and don't introduce new errors. Add new test cases if necessary to cover your changes.

---

Thank you for your interest in contributing to Pygkit! We look forward to collaborating with you and improving the project together.
