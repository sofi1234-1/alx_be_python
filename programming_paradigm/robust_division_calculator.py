# robust_division_calculator.py

def safe_divide(numerator, denominator):
    """
    Safely divides the numerator by the denominator.
    Handles division by zero and non-numeric inputs.
    Returns appropriate messages or the result of division.
    """
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        result = numerator / denominator
        return result
    except ZeroDivisionError:
        return "Error: Cannot divide by zero."
    except ValueError:
        return "Error: Please enter numeric values only."

# Example usage:
if __name__ == "__main__":
    # Test cases
    print("The result of the division is", safe_divide(12, 2))  # Normal division
    print(safe_divide(12, 0))  # Division by zero
    print(safe_divide("twelve", 2))  # Non-numeric input
