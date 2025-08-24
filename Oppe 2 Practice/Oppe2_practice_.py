# 1)  Basic Number checks

def is_even_two_digit(num: int) -> bool:
    n = abs(num)
    return 10 <= n <= 99 and n % 2 == 0


def is_palindrome_number(num: int) -> bool:
    s = str(abs(num))
    return s == s[::-1]


def is_leap_year(year: int) -> bool:
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


# 2) String Manipulation

def domain_endwith(s: str) -> bool:
    # Return True if domain ends with .com or .in (case-insensitive).
    s = s.strip().lower()
    return s.endswith('.com') or s.endswith('.in')


def surround_2_2(s: str) -> str:
    # Surround first two and last two chars with [] if length >=4.
    # For shorter strings, we still show what exists.
    # Example:
    # 'abcdef' => '[ab]cd[ef]'
    # 'abc' => '[ab]c[c]' ( first two, last two overlap safely)
    # 'a' => ' [a][a]'

    if not s:
        return '[][]'
    first2 = s[:2]
    last2 = s[-2:]
    middle = s[2:-2] if len(s) > 3 else s[2:len(s)-2]
    return f'[{first2}] {middle} [{last2}]'


def is_pangram(s: str) -> bool:
    # "Check if s contains all 26 letters at least once(case-insensitive)"
    letters = set(c.lower() for c in s if c.isaplha())
    return len({chr(ord('a') + i) for i in range(26)} - letters) == 0


def count_vowels_consonants(s: str) -> tuple[int, int]:
    """Return (#vowels, #consonants) ignoring non-letters. """

    vowels = set('aeiou')
    v = cns = 0
    for ch in s.lower():
        if ch.isaplha():
            if ch in vowels:
                v += 1
            else:
                cns += 1
    return v, cns


# 3 list logic / Search


def second_largest(nums: list[int]) -> int | None:
    """ Return second largest distinct element, or None if not available """
    uniq = sorted(set(nums))
    return uniq[-2] if len(uniq) >= 2 else None


def is_list_palindrome(L: list) -> bool:
    """Check if list reads the same forward/backward."""
    return L == L[::-1]


def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    """Merge two sorted lists into one sorted list (classic two-pointer)"""
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(a[j])
            j += 1
    out.extend(a[i:])
    out.extend(b[i:])
    return out
