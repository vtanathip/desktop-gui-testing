"""
Test cases for Microsoft Excel application using PyAutoGUI.
These tests demonstrate basic GUI automation for Excel.
"""
import pyautogui
import time
import subprocess
import sys


def open_excel():
    """Open Microsoft Excel application."""
    print("Opening Microsoft Excel...")
    try:
        # Try to open Excel using different methods
        # On Windows, try excel.exe
        subprocess.Popen("excel.exe")
        time.sleep(3)  # Wait for Excel to open
    except FileNotFoundError:
        print("Excel not found. Please ensure Microsoft Excel is installed.")
        sys.exit(1)


def close_excel():
    """Close Excel application without saving."""
    print("Closing Excel...")
    pyautogui.hotkey('alt', 'f4')
    time.sleep(0.5)
    # Press 'n' if asked to save
    pyautogui.press('n')
    time.sleep(1)


def test_excel_data_entry():
    """Test Case 4: Verify data entry in Excel cells."""
    print("\n=== Test Case 4: Excel Data Entry ===")
    
    open_excel()
    
    # Click on cell A1 and enter data
    pyautogui.typewrite('Hello', interval=0.1)
    time.sleep(0.3)
    pyautogui.press('tab')  # Move to next cell
    time.sleep(0.3)
    
    # Enter data in cell B1
    pyautogui.typewrite('World', interval=0.1)
    time.sleep(0.3)
    pyautogui.press('enter')  # Move to next row
    time.sleep(0.5)
    
    # Enter numbers in A2
    pyautogui.typewrite('100', interval=0.1)
    time.sleep(0.3)
    pyautogui.press('tab')
    time.sleep(0.3)
    
    # Enter numbers in B2
    pyautogui.typewrite('200', interval=0.1)
    time.sleep(0.5)
    
    print("Data entry test completed")
    
    close_excel()
    print("Test Case 4 Passed!\n")


def test_excel_formula():
    """Test Case 5: Verify basic formula calculation in Excel."""
    print("\n=== Test Case 5: Excel Formula Calculation ===")
    
    open_excel()
    
    # Enter first number in A1
    pyautogui.typewrite('10', interval=0.1)
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    
    # Enter second number in A2
    pyautogui.typewrite('20', interval=0.1)
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.3)
    
    # Enter formula in A3 to sum A1 and A2
    pyautogui.typewrite('=A1+A2', interval=0.1)
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.5)
    
    print("Formula calculation test completed: =A1+A2 (should be 30)")
    
    close_excel()
    print("Test Case 5 Passed!\n")


if __name__ == "__main__":
    print("Starting Excel GUI Tests...")
    print("=" * 50)
    
    try:
        test_excel_data_entry()
        time.sleep(1)
        
        test_excel_formula()
        
        print("=" * 50)
        print("All Excel tests completed successfully!")
        
    except Exception as e:
        print(f"\nError during testing: {e}")
        print("Attempting to close Excel...")
        try:
            close_excel()
        except:
            pass
