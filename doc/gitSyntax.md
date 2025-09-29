# Commit Message Syntax

Commit messages should follow a clear and standardized convention to ensure readability and traceability of the project. This standard is inspired by [Conventional Commits](https://www.conventionalcommits.org/) and aims to clarify the type of change, its context, and to structure development.

## General Format

- **type**: The type of change (see the list below).
- **scope** (optional): The part of the project affected by the change (e.g., a service, a module).
- **message**: A short description of the changes (in imperative and present tense).

## Commit Types

- **feat**: Addition of a new feature.
  - Example: `feat(user-auth) : add login functionality`

- **fix**: Bug fix.
  - Example: `fix(payment) : fix rounding issue in invoice calculation`

- **chore**: Minor tasks with no impact on application code (e.g., dependency updates).
  - Example: `chore : update dependencies`

- **docs**: Documentation changes.
  - Example: `docs(readme) : add usage instructions`

- **style**: Code style changes (indentation, formatting) with no functional impact.
  - Example: `style : fix indentation`

- **refactor**: Code refactoring without changing behavior.
  - Example: `refactor(order-service) : simplify method flow`

- **test**: Add or modify tests.
  - Example: `test(user-service) : add unit tests`

- **perf**: Performance improvements.
  - Example: `perf(api) : optimize database queries`

- **ci**: Changes related to continuous integration or build tools.
  - Example: `ci : update GitHub Actions configuration`

## Best Practices

- **Clear and precise messages**: The message should be explicit and fit on a single line. Additional details can be included in the commit body.
- **Imperative present tense**: Use imperative present tense to describe what the commit does, e.g., "add", "fix", "update".
- **Optional scope**: The scope is useful to indicate the affected area of the project but can be omitted if not relevant.
- **Avoid vague terms**: Do not use terms like `update`, `change`, or `improve` without specifics.

## Commit Examples

- **Adding a feature**:
