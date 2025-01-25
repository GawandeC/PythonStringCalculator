# string_calculator.py

def add(numbers: str) -> int:
    """
    Calculates the sum of a string of numbers with support for custom delimiters.

    Args:
        numbers (str): A string containing numbers separated by custom delimiters, commas, or newlines.

    Returns:
        int: The sum of the numbers in the string. If the input is empty, returns 0.

    Raises:
        ValueError: If the input contains negative numbers, raises an exception listing all negatives.
    """
    if not numbers:
        return 0

    delimiter = ","
    if numbers.startswith("//"):
        # Extract custom delimiter
        delimiter_section, numbers = numbers.split("\n", 1)
        if delimiter_section.startswith("//[") and delimiter_section.endswith("]"):
            delimiter = delimiter_section[3:-1]  # Delimiters of any length
        else:
            delimiter = delimiter_section[2:]  # Single-character delimiter

    # Replace custom delimiters and newlines with commas
    numbers = numbers.replace("\n", ",").replace(delimiter, ",")

    try:
        number_list = list(map(int, numbers.split(",")))
        negative_numbers = [n for n in number_list if n < 0]
        if negative_numbers:
            raise ValueError(f"Negative numbers not allowed: {','.join(map(str, negative_numbers))}")
        # Ignore numbers larger than 1000
        number_list = [n for n in number_list if n <= 1000]
        return sum(number_list)
    except ValueError as e:
        if "invalid literal" in str(e):
            raise ValueError("Input must be a string of numbers separated by valid delimiters.")
        raise
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
        ("5\n5,5", 15),
        ("//;\n1;2", 3),
        ("//|\n10|20|30", 60),
        ("//#\n2#4#6", 12), 
        ("-1,2,3", "Negative numbers not allowed: -1"),
        ("//;\n-1;2;-3", "Negative numbers not allowed: -1,-3"),
        ("//;\n1000;1001;2", 1002),
        ("999,1000,1001,1", 2000),
        ("//[***]\n1***2***3", 6),
        ("//[&&]\n5&&5&&5", 15),
        ("//[###]\n1000###100###1", 1101)
        
    ]

    for i, (input_data, expected) in enumerate(test_cases):
        try:
            result = add(input_data)
            assert result == expected, f"Test case {i + 1} failed: {input_data} -> {result}"
            print(f"Test case {i + 1} passed: {input_data} -> {result}")
        except AssertionError as e:
            print(e)
        except ValueError as ve:
            assert str(ve) == expected, f"Test case {i + 1} failed: {input_data} -> {ve}"
            print(f"Test case {i + 1} passed: {input_data} -> {ve}")

if __name__ == "__main__":
    main()
