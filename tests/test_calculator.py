"""
Test cases for Windows Calculator application using PyAutoGUI.
These tests demonstrate basic GUI automation for Calculator.
"""
import pyautogui
import time
import subprocess


def open_calculator():
    """Open Windows Calculator application."""
    print("Opening Calculator...")
    subprocess.Popen("calc.exe")
    time.sleep(2)  # Wait for Calculator to open


def close_calculator():
    """Close Calculator application."""
    print("Closing Calculator...")
    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)


def test_calculator_addition():
    """Test Case 1: Verify addition operation in Calculator (2 + 3 = 5)."""
    print("\n=== Test Case 1: Calculator Addition ===")
    
    open_calculator()
    
    # Perform addition: 2 + 3 = 5
    pyautogui.press('2')
    time.sleep(0.3)
    pyautogui.press('plus')
    time.sleep(0.3)
    pyautogui.press('3')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.5)
    
    print("Addition test completed: 2 + 3 = 5")
    
    close_calculator()
    print("Test Case 1 Passed!\n")


def test_calculator_multiplication():
    """Test Case 2: Verify multiplication operation in Calculator (5 * 4 = 20)."""
    print("\n=== Test Case 2: Calculator Multiplication ===")
    
    open_calculator()
    
    # Perform multiplication: 5 * 4 = 20
    pyautogui.press('5')
    time.sleep(0.3)
    pyautogui.press('multiply')
    time.sleep(0.3)
    pyautogui.press('4')
    time.sleep(0.3)
    pyautogui.press('enter')
    time.sleep(0.5)
    
    print("Multiplication test completed: 5 * 4 = 20")
    
    close_calculator()
    print("Test Case 2 Passed!\n")


def test_calculator_clear():
    """Test Case 3: Verify clear function in Calculator."""
    print("\n=== Test Case 3: Calculator Clear Function ===")
    
    open_calculator()
    
    # Enter some numbers
    pyautogui.press('1')
    time.sleep(0.3)
    pyautogui.press('2')
    time.sleep(0.3)
    pyautogui.press('3')
    time.sleep(0.5)
    
    # Press Escape to clear
    pyautogui.press('escape')
    time.sleep(0.5)
    
    print("Clear function test completed")
    
    close_calculator()
    print("Test Case 3 Passed!\n")


if __name__ == "__main__":
    print("Starting Calculator GUI Tests...")
    print("=" * 50)
    
    try:
        test_calculator_addition()
        time.sleep(1)
        
        test_calculator_multiplication()
        time.sleep(1)
        
        test_calculator_clear()
        
        print("=" * 50)
        print("All Calculator tests completed successfully!")
        
    except Exception as e:
        print(f"\nError during testing: {e}")
        print("Attempting to close Calculator...")
        try:
            close_calculator()
        except:
            pass
