# string_calculator.py

def add(numbers: str) -> int:
    """
    Calculates the sum of a string of comma-separated numbers.

    Args:
        numbers (str): A string containing numbers separated by commas.

    Returns:
        int: The sum of the numbers in the string. If the input is empty, returns 0.
    """
    if not numbers:
        return 0

    # Split the string into a list of numbers, convert to integers, and calculate the sum
    try:
        numbers = numbers.replace("\n", ",")
        number_list = map(int, numbers.split(","))
        return sum(number_list)
    except ValueError:
        raise ValueError("Input must be a string of comma- or newline-separated integers.")

# Tests for the string calculator
def main():
    test_cases = [
        ("", 0),
        ("1", 1),
        ("1,5", 6),
        ("2,3,10", 15),
        ("10,20,30", 60),
        ("1\n2,3", 6),
        ("1\n2\n3", 6),
        ("5\n5,5", 15)
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        try:
            result = add(input_data)
            assert result == expected, f"Test case {i + 1} failed: {input_data} -> {result}"
            print(f"Test case {i + 1} passed: {input_data} -> {result}")
        except AssertionError as e:
            print(e)
        except ValueError as ve:
            print(f"Test case {i + 1} failed: {ve}")

if __name__ == "__main__":
    main()
