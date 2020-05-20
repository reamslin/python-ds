def valid_parentheses(parens):
    """Are the parentheses validly balanced?

        >>> valid_parentheses("()")
        True

        >>> valid_parentheses("()()")
        True

        >>> valid_parentheses("(()())")
        True

        >>> valid_parentheses(")()")
        False

        >>> valid_parentheses("())")
        False

        >>> valid_parentheses("((())")
        False

        >>> valid_parentheses(")()(")
        False
    """
    unclosed = 0
    for p in parens:
        if unclosed < 0:
            return False
        else:
            if p == "(":
                unclosed += 1
            elif p == ")":
                unclosed -= 1
    return unclosed == 0
