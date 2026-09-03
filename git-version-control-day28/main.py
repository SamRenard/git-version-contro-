def process_data(input_value: int, multiplier: int = 2) -> int:
    """
    Processes the input value by multiplying it.
    """
    return input_value * multiplier

if __name__ == "__main__":
    result = process_data(input_value=15)
    print(f"Processed output: {result}")