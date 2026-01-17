---
name: test-execution
description: Executes pytest tests for the backend using 'uv' and playwright tests for the frontend. Supports running the full suite, specific test files, and backend coverage reports. Use this skill when you need to run tests, verify changes, or check code coverage.
---

# Test Execution Skill

This skill provides a reliable way to run pytest tests within the `/backend` directory using `uv`, and playwright tests within the `/frontend` directory.

## Prerequisites

- **Backend:** `uv` installed and `backend` directory present.
- **Frontend:** `node` and `playwright` dependencies installed (`frontend/node_modules`).

## Usage

Use the bundled script `.opencode/skills/test-execution/scripts/run_tests.sh` to execute the tests.

### 1. Run Backend Tests

To execute the full backend test suite:

```bash
.opencode/skills/test-execution/scripts/run_tests.sh backend
```

#### Run a Specific Backend Test File

```bash
.opencode/skills/test-execution/scripts/run_tests.sh backend tests/test_auth.py
```

#### Generate Backend Coverage Report

```bash
.opencode/skills/test-execution/scripts/run_tests.sh backend --cov
```

### 2. Run Frontend Tests

To execute the frontend (playwright) test suite:

```bash
.opencode/skills/test-execution/scripts/run_tests.sh frontend
```

#### Run a Specific Frontend Test File

```bash
.opencode/skills/test-execution/scripts/run_tests.sh frontend e2e/auth.spec.ts
```
