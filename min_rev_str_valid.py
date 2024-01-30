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
    reversals if string is valid (even length)
    else returns -1
    """
    input_str = input_str.strip()
    count: int = 0
    stack: List = []

    # If odd length string, then return -1
    if len(input_str) % 2 != 0:
        return -1

    for bracket in input_str:
        if bracket == '[':
            stack.append('[')
        elif bracket == ']':
            if not stack:
                stack.append('[')
                count += 1
            else:
                stack.pop()
    count += len(stack)//2
    return count


if __name__ == "__main__":
    expr = "[[[[]]"
    result = find_min_rev(expr)
    print(result)
