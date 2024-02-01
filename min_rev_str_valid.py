"""
Problem: Minimum number of bracket
reversals needed to make an expression balanced
"""

from typing import List


def find_min_rev(input_str: str) -> int:
    """
    Minimum number of bracket reversals
    needed to make an expression balanced
    
    Returns the minimum number of bracket
    reversals if the string is valid (even length)
    else returns -1
    """

    # Remove leading and trailing whitespaces from the input string
    input_str = input_str.strip()

    # Initialize a counter variable to keep track of the number of reversals
    count: int = 0

    # Initialize an empty list to simulate a stack for tracking brackets
    stack: List = []

    # If the length of the string is odd, it's impossible to balance, return -1
    if len(input_str) % 2 != 0:
        return -1

    # Iterate through each character in the input string
    for bracket in input_str:
        # If the current character is an opening bracket '['
        if bracket == '[':
            # Push it onto the stack
            stack.append('[')
        # If the current character is a closing bracket ']'
        elif bracket == ']':
            # If the stack is empty, meaning there is no matching opening bracket for the current closing bracket
            if not stack:
                # Add an opening bracket to the stack to pair with the current closing bracket
                stack.append('[')

                # Increment the count, as a reversal is needed to balance the brackets
                count += 1
            else:
                # Pop the matching opening bracket from the stack
                stack.pop()

    # Increment the count by half of the remaining stack length to pair unmatched opening brackets
    count += len(stack) // 2

    # Return the minimum number of bracket reversals needed
    return count


# Example usage
if __name__ == "__main__":
    expr = "]]]["
    result = find_min_rev(expr)
    print(result)
