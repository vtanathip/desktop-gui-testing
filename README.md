# desktop-gui-testing

Sample application for testing desktop GUI applications using PyAutoGUI and UV package manager.

## Overview

This project demonstrates automated GUI testing for desktop applications using Python and PyAutoGUI. It includes 5 test cases:
- 3 test cases for **Windows Calculator**
- 2 test cases for **Microsoft Excel**

## Prerequisites

- Python 3.12 or higher
- UV package manager
- Windows OS (for Calculator and Excel)
- Microsoft Excel installed (for Excel tests)

## Installation

1. Install UV package manager (if not already installed):
```bash
pip install uv
```

2. Clone the repository:
```bash
git clone https://github.com/vtanathip/desktop-gui-testing.git
cd desktop-gui-testing
```

3. Install dependencies using UV:
```bash
uv sync
```

## Running Tests

### Run All Tests
To run all 5 test cases sequentially:
```bash
uv run run_tests.py
```

### Run Individual Test Suites

**Calculator Tests Only:**
```bash
uv run python tests/test_calculator.py
```

**Excel Tests Only:**
```bash
uv run python tests/test_excel.py
```

## Test Cases

### Calculator Tests

1. **Test Case 1: Addition** - Tests basic addition operation (2 + 3 = 5)
2. **Test Case 2: Multiplication** - Tests multiplication operation (5 * 4 = 20)
3. **Test Case 3: Clear Function** - Tests the clear/escape functionality

### Excel Tests

4. **Test Case 4: Data Entry** - Tests entering text and numbers in cells
5. **Test Case 5: Formula Calculation** - Tests basic formula calculation (=A1+A2)

## Important Notes

⚠️ **During Test Execution:**
- Do NOT use your mouse or keyboard while tests are running
- Tests will automatically open and close applications
- Keep your screen visible and unlocked
- Excel tests will close without saving changes

## Project Structure

```
desktop-gui-testing/
├── tests/
│   ├── __init__.py
│   ├── test_calculator.py  # Calculator test cases
│   └── test_excel.py       # Excel test cases
├── run_tests.py            # Main test runner
├── pyproject.toml          # UV project configuration
├── uv.lock                 # UV dependency lock file
├── .python-version         # Python version specification
└── README.md               # This file
```

## Dependencies

- **pyautogui** - For GUI automation
- **pillow** - For screenshot functionality (used by PyAutoGUI)

All dependencies are managed by UV and specified in `pyproject.toml`.

## License

MIT License - See LICENSE file for details.

