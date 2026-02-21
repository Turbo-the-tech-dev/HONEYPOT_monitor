# Contributing to HONEYPOT_monitor

We welcome contributions to the `HONEYPOT_monitor` project! Your help is invaluable in building robust tools for ethical honeypot monitoring and threat intelligence gathering.

Please take a moment to review this document to understand how to contribute effectively and adhere to our project's principles.

## How to Report Issues

If you find a bug, have a feature request, or notice something isn't working as expected, please open an issue on our [GitHub Issues page](https://github.com/Turbo-the-tech-dev/HONEYPOT_monitor/issues).

When reporting an issue, please:

*   **Use Issue Templates:** Whenever available, please use the provided issue templates (e.g., Bug Report, Feature Request) to ensure all necessary information is included.
*   **Be Specific:** Clearly describe the problem or suggestion.
*   **Include Steps to Reproduce:** For bugs, provide clear, step-by-step instructions that can reproduce the issue. Include screenshots or code snippets if helpful.
*   **Environment Details:** Mention your operating system, Python version, and any other relevant environment details.

## How to Submit Pull Requests (PRs)

We love pull requests! If you'd like to contribute code, please follow these steps:

1.  **Fork the Repository:** Start by forking the `HONEYPOT_monitor` repository to your GitHub account.
2.  **Create a New Branch:** Create a new branch from `main` for your feature or bug fix. Use a descriptive name (e.g., `feature/add-new-logger`, `bugfix/ssh-disconnect-error`).
    ```bash
    git checkout main
    git pull origin main
    git checkout -b your-branch-name
    ```
3.  **Make Your Changes:** Implement your feature or fix the bug.
4.  **Write Tests:** Ensure your changes are covered by appropriate unit tests.
5.  **Ensure Code Style:** Follow our code style guidelines (see below).
6.  **Update Documentation:** If your changes affect how the project is used or configured, update the `README.md` or other relevant documentation.
7.  **Descriptive Title:** Provide a clear and concise title for your pull request.
8.  **Link to Issue:** In your PR description, reference the issue your PR addresses (e.g., `Closes #123`, `Fixes #45`).
9.  **Submit Your PR:** Push your branch to your fork and open a pull request against the `main` branch of the original `HONEYPOT_monitor` repository.

## Ethical Guidelines for Honeypot Contributions

The `HONEYPOT_monitor` project is built on principles of ethical and defensive security research. All contributions **must** adhere to these guidelines:

*   **Defensive Only:** All code and features must be for defensive purposes, aimed at monitoring, logging, and analyzing threats.
*   **No Attack Vectors:** Do **not** include any code that could be used as an offensive tool, exploit vulnerabilities, or facilitate attacks.
*   **Report Findings Responsibly:** If you discover vulnerabilities while working on honeypots, report them responsibly through appropriate channels.

## Code Style

*   **PEP 8 Compliance:** All Python code must adhere to [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guidelines. We encourage the use of linters (e.g., `flake8`, `pylint`) to check your code.
*   **Readability:** Write clear, concise, and well-commented code.

## Testing

*   **Unit Tests:** All new features and bug fixes should be accompanied by relevant unit tests to ensure correctness and prevent regressions.
*   **Integration Tests:** Integration tests are highly encouraged for components that interact with multiple parts of the system or external services.

Thank you for contributing to `HONEYPOT_monitor`!
