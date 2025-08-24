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

 # second method to solve this

 return sorted(a + b)
    

# 4. Counting with Conditions

def count_odd_three_digit(items: list[int | None]) -> int:
    """Count how many values are odd three-digit numbers (ignore sign, skip None)."""

    cnt = 0
    for x in items:
        if x is None:
            continue
    n = abs(int(x))
    if 100 <= n <= 999 and n % 2 == 1:
        cnt += 1
    return cnt



def count_perfect_squares(nums: list[int]) -> int:
    """Count numbers that are perfect squares (n >= 0.)"""

    import math
    cnt = 0
    for n in nums:
        if n >= 0:
            r = int(math.isqrt(n))
            if r * r == n:
                cnt += 1
    return cnt
    

def count_names_start_with_vowel(names: list[str]) -> int:
    """Count names whose first letter is a vowel (case-insensitive)."""
    vowels = set('aeiou')
    return sum(1 for name in names if name and name[0].lower() in vowels)


# 5. Input / Output (Formatting) - typically console tasks 

def name_to_initials(full_name: str) -> str:
    """ "John Ronald Reuel Tolkien" -> "J. R. R. Tolkien"
    Last word stays as last name; other becomes initials with '.' """

    parts = [p for p in full_name.split() if p]
    if not parts:
        return ''
    if len(parts) == 1:
        return parts[0]
    last = parts[-1]
    initials = ' '.join([p[0].upper() + '.' for p in parts[:-1]])
    return f"{initials}{last}"