class Trie:
    def __init__(self):
        self.data = {}

    def add(self, word):
        ref = self.data
        for char in word:
            ref[char] = char in ref and ref[char] or {}
            ref = ref[char]
        ref[""] = 1

    def dump(self):
        return self.data

    def quote(self, char):
        return char

    def _pattern(self, pData):
        data = pData
        if "" in data and len(data.keys()) == 1:
            return None

        alt = []
        cc = []
        q = 0
        for char in sorted(data.keys()):
            if isinstance(data[char], dict):
                try:
                    recurse = self._pattern(data[char])
                    alt.append(self.quote(char) + recurse)
                except:
                    cc.append(self.quote(char))
            else:
                q = 1
        cconly = not len(alt) > 0

        if len(cc) > 0:
            if len(cc) == 1:
                alt.append(cc[0])
            else:
                alt.append("[" + "".join(cc) + "]")

        if len(alt) == 1:
            result = alt[0]
        else:
            result = "(?:" + "|".join(alt) + ")"

        if q:
            if cconly:
                result += "?"
            else:
                result = "(?:%s)?" % result
        return result

    def pattern(self):
        return self._pattern(self.dump()).replace("\\-", "-")


def number_between(start, end, fullnumberreplacement="\\d"):
    r"""
    Generate a regular expression to match numbers within a specified range.

    Args:
        start (int): The start of the range.
        end (int): The end of the range.
        fullnumberreplacement (str): Replacement for digits (0-9) in the regular expression pattern.

    Returns:
        str: The regular expression pattern to match numbers within the specified range.
    """
    tree = Trie()
    if start >= 0 and end >= 0:
        for x in range(start, end):
            tree.add(str(x))
        return (
            "(?:(?<!-)\\b(?:"
            + tree.pattern().replace("[0123456789]", fullnumberreplacement)
            + ")\\b)"
        )
    if start < 0 and end < 0:
        for x in range(start, end):
            tree.add(str(-x))
        return (
            "(?:(?:-\\b"
            + tree.pattern().replace("[0123456789]", fullnumberreplacement)
            + ")\\b)"
        )
    if start < 0 and end >= 0:
        for x in range(start, 0):
            tree.add(str(-x))
        re1 = (
            "(?:-(?:\\b"
            + tree.pattern().replace("[0123456789]", fullnumberreplacement)
            + ")\\b)"
        )
        tree2 = Trie()
        for x in range(0, end):
            tree2.add(str(x))
        re2 = (
            "(?:(?<!-)\\b(?:"
            + tree2.pattern().replace("[0123456789]", fullnumberreplacement)
            + ")\\b)"
        )
        return f"{re1}|{re2}"
    else:
        for x in range(start, end):
            tree.add(str(-x))
        return (
            "(?:\\b(?:"
            + tree.pattern().replace("[0123456789]", fullnumberreplacement)
            + ")\\b)"
        )


def number_ge(n, fullnumberreplacement="\\d"):
    r"""
    Generate a regular expression to match numbers greater than or equal to a specified value.

    Args:
        n (int): The value to compare against.
        fullnumberreplacement (str): Replacement for digits (0-9) in the regular expression pattern.

    Returns:
        str: The regular expression pattern to match numbers greater than or equal to the specified value.
    """
    if n >= 0:
        number_of_digits = len(str(n))
        tree = Trie()
        for x in range(n, int("1" + "0" * number_of_digits)):
            tree.add(str(x))
        return (
            "(?:(?<!-)(?:\\b"
            + tree.pattern().replace("[0123456789]", fullnumberreplacement)
            + f"\\b))|(?:(?<!-)(?:\\b[1-9]{fullnumberreplacement}{{{number_of_digits},}}\\b))"
        )
    else:
        tree = Trie()
        for x in range(n, 0):
            tree.add(str(-x))
        return (
            "(?:-(?:\\b"
            + tree.pattern().replace("[0123456789]", fullnumberreplacement)
            + f"\\b))|(?:\\b0\\b)|(?:(?<!-)(?:\\b[1-9]{fullnumberreplacement}{{0,}}\\b))"
        )


def number_le(n, fullnumberreplacement="\\d"):
    r"""
    Generate a regular expression to match numbers less than or equal to a specified value.

    Args:
        n (int): The value to compare against.
        fullnumberreplacement (str): Replacement for digits (0-9) in the regular expression pattern.

    Returns:
        str: The regular expression pattern to match numbers less than or equal to the specified value.
    """
    if n < 0:
        number_of_digits = len(str(n)) - 1
        tree = Trie()
        for x in range(-n, int("1" + "0" * (number_of_digits - 1) + "1")):
            tree.add(str(x))
        return (
            "(?:-(?:\\b"
            + tree.pattern().replace("[0123456789]", fullnumberreplacement)
            + f"\\b))|(?:-\\b[1-9]{fullnumberreplacement}{{{number_of_digits},}}\\b)"
        )

    else:
        number_of_digits = len(str(n)) - 1
        tree = Trie()
        for x in range(n, 0, -1):
            tree.add(str(x))
        return (
            "(?:(?:\\b"
            + tree.pattern().replace("[0123456789]", fullnumberreplacement)
            + f"\\b))|(?:\\b0\\b)|(?:-\\b[1-9]{fullnumberreplacement}{{0,}}\\b)"
        )
