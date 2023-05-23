def upper_string(input_string):
    """convert string to Upper """
    return input_string.upper()


def capitalize_words(input_string):
    """
    Capitalizes the first letter of each word in the input string.

    Args:
        input_string (str): The input string.

    Returns:
        str: The input string with the first letter of each word capitalized.
    """
    words = input_string.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)