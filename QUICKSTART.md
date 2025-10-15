# Quick Start Guide

## Setup (One-time)

1. Install UV:
   ```bash
   pip install uv
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

## Running Tests

### All Tests
```bash
uv run run_tests.py
```

### Calculator Only
```bash
uv run python tests/test_calculator.py
```

### Excel Only
```bash
uv run python tests/test_excel.py
```

## What to Expect

- Tests will automatically open Calculator/Excel
- Watch as PyAutoGUI controls the applications
- Applications will close automatically after each test
- **Do not touch mouse/keyboard during execution**

## Test Cases

| # | Application | Test Description |
|---|-------------|------------------|
| 1 | Calculator  | Addition (2+3=5) |
| 2 | Calculator  | Multiplication (5×4=20) |
| 3 | Calculator  | Clear function |
| 4 | Excel       | Data entry in cells |
| 5 | Excel       | Formula calculation (=A1+A2) |

## Troubleshooting

**Excel not found?**
- Ensure Microsoft Excel is installed
- Test will exit with error if Excel is not available

**Tests failing?**
- Don't use mouse/keyboard during test execution
- Ensure screen is unlocked and visible
- Close any dialogs or popups before running

**Import errors?**
- Run `uv sync` to install dependencies
- Verify Python 3.12+ is installed
