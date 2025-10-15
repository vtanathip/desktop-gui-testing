"""
Main test runner for desktop GUI testing.
This script runs all GUI test cases for Calculator and Excel applications.
"""
import sys
import time
from tests.test_calculator import (
    test_calculator_addition,
    test_calculator_multiplication,
    test_calculator_clear
)
from tests.test_excel import (
    test_excel_data_entry,
    test_excel_formula
)


def run_all_tests():
    """Run all GUI test cases."""
    print("=" * 60)
    print("DESKTOP GUI TESTING - Test Suite")
    print("=" * 60)
    print("\nThis test suite will run 5 test cases:")
    print("  - 3 test cases for Calculator")
    print("  - 2 test cases for Microsoft Excel")
    print("\nPlease do not use mouse/keyboard during tests.")
    print("Press Ctrl+C to cancel...")
    print("=" * 60)
    
    time.sleep(3)  # Give user time to read
    
    failed_tests = []
    
    # Calculator Tests
    print("\n\n### CALCULATOR TESTS ###\n")
    try:
        test_calculator_addition()
        time.sleep(1)
    except Exception as e:
        print(f"Test Failed: {e}")
        failed_tests.append("test_calculator_addition")
    
    try:
        test_calculator_multiplication()
        time.sleep(1)
    except Exception as e:
        print(f"Test Failed: {e}")
        failed_tests.append("test_calculator_multiplication")
    
    try:
        test_calculator_clear()
        time.sleep(1)
    except Exception as e:
        print(f"Test Failed: {e}")
        failed_tests.append("test_calculator_clear")
    
    # Excel Tests
    print("\n\n### EXCEL TESTS ###\n")
    try:
        test_excel_data_entry()
        time.sleep(1)
    except Exception as e:
        print(f"Test Failed: {e}")
        failed_tests.append("test_excel_data_entry")
    
    try:
        test_excel_formula()
        time.sleep(1)
    except Exception as e:
        print(f"Test Failed: {e}")
        failed_tests.append("test_excel_formula")
    
    # Summary
    print("\n" + "=" * 60)
    print("TEST SUMMARY")
    print("=" * 60)
    
    total_tests = 5
    passed_tests = total_tests - len(failed_tests)
    
    print(f"Total Tests: {total_tests}")
    print(f"Passed: {passed_tests}")
    print(f"Failed: {len(failed_tests)}")
    
    if failed_tests:
        print("\nFailed Tests:")
        for test in failed_tests:
            print(f"  - {test}")
    else:
        print("\n✓ All tests passed successfully!")
    
    print("=" * 60)


if __name__ == "__main__":
    try:
        run_all_tests()
    except KeyboardInterrupt:
        print("\n\nTests cancelled by user.")
        sys.exit(0)
    except Exception as e:
        print(f"\n\nUnexpected error: {e}")
        sys.exit(1)
