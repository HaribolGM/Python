
# OPPE 2 — Python Master Cheat Sheet
# ----------------------------------
# Everything is written as reusable functions with *clear* comments.
# You can paste a function into the editor when a similar pattern appears.
#
# IMPORTANT: Many OPPE tasks only want the function definition (no input/print).
# I follow that convention below unless the pattern explicitly asks for console I/O.
#
# Contents
#   0) Handy utilities (prime test, gcd, file helpers)
#   1) Basic Number Checks
#   2) String Manipulation
#   3) List Logic / Search
#   4) Counting with Conditions
#   5) Input/Output formatting (names → initials etc.)
#   6) Dictionary + Sorting
#   7) File/Text Processing (text files)
#   8) CSV Processing (student dataset)
#   9) Math / Transformations
#  10) Matrices (sum/product)
#  11) Recursion pack (combos, perms, gcd, sum-digits, prime, count-char)
#  12) Prime numbers at prime indices
#
# -------------------------------------------------------------
# 0) Utilities
# -------------------------------------------------------------

import csv


def is_prime(n: int) -> bool:
    """Return True if n is prime (n >= 2), else False.
    Works in O(sqrt(n))."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    # Only odd divisors up to sqrt(n)
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def gcd(a: int, b: int) -> int:
    """Greatest common divisor via Euclid's algorithm."""
    while b != 0:
        a, b = b, a % b
    return abs(a)


# -------------------------------------------------------------
# 1) Basic Number Checks
# -------------------------------------------------------------

def is_even_two_digit(num: int) -> bool:
    """Check if |num| is an even two-digit number (10..99)."""
    n = abs(num)
    return 10 <= n <= 99 and n % 2 == 0


def is_palindrome_number(num: int) -> bool:
    """Check if number is palindrome (considering optional leading '-').
    We compare by string on absolute value."""
    s = str(abs(num))
    return s == s[::-1]


def is_leap_year(year: int) -> bool:
    """Leap year rule."""
    return (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)


# -------------------------------------------------------------
# 2) String Manipulation
# -------------------------------------------------------------

def domain_endswith(s: str) -> bool:
    """Return True if domain ends with .com or .in (case-insensitive)."""
    s = s.strip().lower()
    return s.endswith('.com') or s.endswith('.in')


def surround_2_2(s: str) -> str:
    """Surround first two and last two chars with [] if length >= 4.
    For shorter strings, we still show what exists.
    Examples:
      'abcdef' -> '[ab]cd[ef]'
      'abc'    -> '[ab]c[c]' (first two, last two overlap safely)
      'a'      -> '[a][a]'
    """
    if not s:
        return '[][]'
    first2 = s[:2]
    last2 = s[-2:]
    middle = s[2:-2] if len(s) > 3 else s[2:len(s)-2]
    return f'[{first2}]{middle}[{last2}]'


def is_pangram(s: str) -> bool:
    """Check if s contains all 26 letters at least once (case-insensitive)."""
    letters = set(c.lower() for c in s if c.isalpha())
    return len({chr(ord('a') + i) for i in range(26)} - letters) == 0


def count_vowels_consonants(s: str) -> tuple[int, int]:
    """Return (#vowels, #consonants) ignoring non-letters."""
    vowels = set('aeiou')
    v = cns = 0
    for ch in s.lower():
        if ch.isalpha():
            if ch in vowels:
                v += 1
            else:
                cns += 1
    return v, cns


# -------------------------------------------------------------
# 3) List Logic / Search
# -------------------------------------------------------------

def second_largest(nums: list[int]) -> int | None:
    """Return second largest distinct element, or None if not available."""
    uniq = sorted(set(nums))
    return uniq[-2] if len(uniq) >= 2 else None


def is_list_palindrome(L: list) -> bool:
    """Check if list reads the same forward/backward."""
    return L == L[::-1]


def merge_sorted(a: list[int], b: list[int]) -> list[int]:
    """Merge two sorted lists into one sorted list (classic two-pointer)."""
    i = j = 0
    out = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            out.append(a[i])
            i += 1
        else:
            out.append(b[j])
            j += 1
    out.extend(a[i:])
    out.extend(b[j:])
    return out


# -------------------------------------------------------------
# 4) Counting with Conditions
# -------------------------------------------------------------

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
    """Count numbers that are perfect squares (n >= 0)."""
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


# -------------------------------------------------------------
# 5) Input/Output (formatting) — typically console tasks
# -------------------------------------------------------------

def name_to_initials(full_name: str) -> str:
    """"John Ronald Reuel Tolkien" -> "J. R. R. Tolkien"
    Last word stays as last name; others become initials with '.'"""
    parts = [p for p in full_name.split() if p]
    if not parts:
        return ''
    if len(parts) == 1:
        return parts[0]
    last = parts[-1]
    initials = ' '.join(p[0].upper() + '.' for p in parts[:-1])
    return f"{initials} {last}"


def sort_fullnames_as_initials(names: list[str]) -> list[str]:
    """Convert list of full names to 'initials + last' and sort alphabetically by last name."""
    converted = [(name_to_initials(n), n.split()[-1])
                 for n in names if n.strip()]
    converted.sort(key=lambda t: t[1].lower())
    return [t[0] for t in converted]


# -------------------------------------------------------------
# 6) Dictionary + Sorting
# -------------------------------------------------------------

def grocery_total_bill(items: list[dict]) -> float:
    """Each item: {"name": str, "quantity": int, "price": float}. Return total bill."""
    return sum(it.get("quantity", 0) * it.get("price", 0.0) for it in items)


def grocery_item_with_max_quantity(items: list[dict]) -> dict | None:
    """Return item dict with maximum quantity (tie: first)."""
    return max(items, key=lambda it: it.get("quantity", 0), default=None)


def sort_grocery_by_total_amount(items: list[dict]) -> list[dict]:
    """Sort by (price*quantity) ascending; change 'key=' for descending if needed."""
    return sorted(items, key=lambda it: it.get("quantity", 0) * it.get("price", 0.0))


# -------------------------------------------------------------
# 7) File/Text Processing (text files)
# -------------------------------------------------------------

def longest_word_in_file(filename: str) -> str:
    """Return the longest word (ties: first found). Non-letters allowed; split on whitespace."""
    longest = ''
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            for w in line.split():
                if len(w) > len(longest):
                    longest = w
    return longest


def remove_blank_lines(infile: str, outfile: str) -> None:
    """Copy infile -> outfile without blank lines (lines with only whitespace)."""
    with open(infile, 'r', encoding='utf-8') as fin, open(outfile, 'w', encoding='utf-8') as fout:
        for line in fin:
            if line.strip():
                fout.write(line)


def find_and_replace(infile: str, outfile: str, target: str, replacement: str) -> None:
    """Replace all occurrences of 'target' with 'replacement' and write to outfile."""
    with open(infile, 'r', encoding='utf-8') as fin, open(outfile, 'w', encoding='utf-8') as fout:
        for line in fin:
            fout.write(line.replace(target, replacement))


def sort_words_in_file(infile: str, outfile: str) -> None:
    """Read all words, sort alphabetically (case-insensitive), write one per line."""
    words = []
    with open(infile, 'r', encoding='utf-8') as f:
        for line in f:
            words.extend(line.split())
    words.sort(key=str.lower)
    with open(outfile, 'w', encoding='utf-8') as f:
        for w in words:
            f.write(w + '\n')


def word_frequency_to_file(infile: str, outfile: str) -> None:
    """Count word frequencies and store sorted by frequency (desc), then word (asc)."""
    from collections import Counter
    words = []
    with open(infile, 'r', encoding='utf-8') as f:
        for line in f:
            words.extend(line.split())
    freq = Counter(w.lower() for w in words)
    # Sort by (-count, word)
    items = sorted(freq.items(), key=lambda t: (-t[1], t[0]))
    with open(outfile, 'w', encoding='utf-8') as f:
        for w, c in items:
            f.write(f"{w},{c}\n")


# -------------------------------------------------------------
# 8) CSV Processing (student dataset)
#     Expected headers (case-sensitive in this template):
#     Name,Gender,Branch,GPA,Age
# -------------------------------------------------------------


def _read_students(csv_filename: str) -> list[dict]:
    """Read CSV and coerce types for GPA (float) and Age (int)."""
    rows = []
    with open(csv_filename, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # Keep original strings for Name, Gender, Branch.
            # Convert GPA and Age where present.
            if 'GPA' in row and row['GPA'] != '':
                row['GPA'] = float(row['GPA'])
            if 'Age' in row and row['Age'] != '':
                row['Age'] = int(row['Age'])
            rows.append(row)
    return rows


def avg_gpa_males_in_cs(csv_filename: str) -> float | None:
    data = _read_students(csv_filename)
    vals = [r['GPA'] for r in data
            if r.get('Gender', '').lower().startswith('m')
            and r.get('Branch', '').lower() == 'computer science'
            and isinstance(r.get('GPA'), float)]
    return sum(vals)/len(vals) if vals else None


def youngest_female_in_ee(csv_filename: str) -> str | None:
    data = _read_students(csv_filename)
    females_ee = [r for r in data
                  if r.get('Gender', '').lower().startswith('f')
                  and r.get('Branch', '').lower() == 'electrical engineering'
                  and isinstance(r.get('Age'), int)]
    if not females_ee:
        return None
    return min(females_ee, key=lambda r: r['Age']).get('Name')


def sort_by_branch_then_gpa(csv_filename: str, outfile: str) -> None:
    data = _read_students(csv_filename)
    data.sort(key=lambda r: (r.get('Branch', ''), -
              (r.get('GPA') if isinstance(r.get('GPA'), float) else -1e9)))
    # Write CSV back
    if data:
        fieldnames = list(data[0].keys())
        with open(outfile, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(data)


def bump_gpa_chemical(csv_filename: str, outfile: str) -> None:
    data = _read_students(csv_filename)
    for r in data:
        if r.get('Branch', '').lower() == 'chemical engineering' and isinstance(r.get('GPA'), float):
            r['GPA'] = min(r['GPA'] + 0.5, 10.0)  # Cap at 10 if needed
    if data:
        fieldnames = list(data[0].keys())
        with open(outfile, 'w', newline='', encoding='utf-8') as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(data)


def count_males_per_branch(csv_filename: str) -> dict:
    data = _read_students(csv_filename)
    out = {}
    for r in data:
        if r.get('Gender', '').lower().startswith('m'):
            br = r.get('Branch', '')
            out[br] = out.get(br, 0) + 1
    return out


def avg_gpa_by_branch(csv_filename: str, branch: str) -> float | None:
    data = _read_students(csv_filename)
    b = branch.strip().lower()
    vals = [r['GPA'] for r in data if r.get(
        'Branch', '').lower() == b and isinstance(r.get('GPA'), float)]
    return sum(vals)/len(vals) if vals else None


def top_by_gender(csv_filename: str, gender: str) -> str | None:
    data = _read_students(csv_filename)
    g = gender.strip().lower()
    cand = [r for r in data if r.get('Gender', '').lower(
    ).startswith(g) and isinstance(r.get('GPA'), float)]
    if not cand:
        return None
    return max(cand, key=lambda r: r['GPA']).get('Name')


def names_in_age_range_sorted_by_gpa(csv_filename: str, age_lo: int, age_hi: int) -> list[str]:
    data = _read_students(csv_filename)
    cand = [r for r in data
            if isinstance(r.get('Age'), int) and age_lo <= r['Age'] <= age_hi and isinstance(r.get('GPA'), float)]
    cand.sort(key=lambda r: -r['GPA'])
    return [r.get('Name') for r in cand]


def topper_in_branch(csv_filename: str, branch: str) -> str | None:
    data = _read_students(csv_filename)
    b = branch.strip().lower()
    cand = [r for r in data if r.get('Branch', '').lower(
    ) == b and isinstance(r.get('GPA'), float)]
    if not cand:
        return None
    return max(cand, key=lambda r: r['GPA']).get('Name')


def names_above_gpa_sorted_by_age(csv_filename: str, cutoff: float) -> list[str]:
    data = _read_students(csv_filename)
    cand = [r for r in data if isinstance(
        r.get('GPA'), float) and r['GPA'] > cutoff and isinstance(r.get('Age'), int)]
    cand.sort(key=lambda r: r['Age'])
    return [r.get('Name') for r in cand]


# -------------------------------------------------------------
# 9) Math / Transformations
# -------------------------------------------------------------

def sum_floored_to_nearest_10(a: int, b: int) -> int:
    """Return floor((a+b)/10)*10 without using // for the rounding logic."""
    s = a + b
    return (s // 10) * 10


def product_of_digits(n: int) -> int:
    """Product of digits of |n| (0 if n==0)."""
    n = abs(n)
    if n == 0:
        return 0
    prod = 1
    while n > 0:
        prod *= (n % 10)
        n //= 10
    return prod


def decimal_to_binary(n: int) -> str:
    """Convert integer to binary (no bin())."""
    if n == 0:
        return '0'
    neg = n < 0
    n = abs(n)
    bits = []
    while n > 0:
        bits.append(str(n % 2))
        n //= 2
    out = ''.join(reversed(bits))
    return '-' + out if neg else out


def digital_root(n: int) -> int:
    """Sum digits repeatedly until a single digit remains."""
    n = abs(n)
    while n >= 10:
        s = 0
        while n > 0:
            s += n % 10
            n //= 10
        n = s
    return n


# -------------------------------------------------------------
# 10) Matrices
# -------------------------------------------------------------

def mat_sum(A: list[list[int | float]], B: list[list[int | float]], C: list[list[int | float]]):
    """Return A + B + C if same dimensions, else -1."""
    if not A or not B or not C:
        return -1
    m, n = len(A), len(A[0])
    if len(B) != m or len(C) != m or any(len(row) != n for row in B) or any(len(row) != n for row in C):
        return -1
    out = [[A[i][j] + B[i][j] + C[i][j] for j in range(n)] for i in range(m)]
    return out


def mat_mul(X: list[list[int | float]], Y: list[list[int | float]]):
    """Matrix multiplication X @ Y (dimensions must align)."""
    m, k = len(X), len(X[0])
    k2, n = len(Y), len(Y[0])
    assert k == k2, 'Inner dimensions must match'
    # Precompute columns of Y for speed
    cols = list(zip(*Y))  # shape (n, k)
    out = [[sum(X[i][t] * cols[j][t] for t in range(k))
            for j in range(n)] for i in range(m)]
    return out


def mat_product(A, B, C, D, E):
    """Return A*B*C*D*E (all square, same size, as per problem)."""
    return mat_mul(mat_mul(mat_mul(mat_mul(A, B), C), D), E)


# -------------------------------------------------------------
# 11) Recursion pack
# -------------------------------------------------------------

def combinations(nums: list[int]) -> list[list[int]]:
    """All combinations (subsets) via recursion.
    Order: by decision tree, starting with []."""
    out = []

    def rec(i: int, cur: list[int]):
        if i == len(nums):
            out.append(cur.copy())
            return
        # Exclude nums[i]
        rec(i+1, cur)
        # Include nums[i]
        cur.append(nums[i])
        rec(i+1, cur)
        cur.pop()
    rec(0, [])
    # Optional: sort each subset, then sort all by length/lex if a fixed order is needed.
    return out


def permutations_str(s: str) -> list[str]:
    """All permutations of a string via recursion."""
    out = []

    def rec(prefix: str, rest: str):
        if not rest:
            out.append(prefix)
            return
        for i, ch in enumerate(rest):
            rec(prefix + ch, rest[:i] + rest[i+1:])
    rec('', s)
    return out


def gcd_rec(a: int, b: int) -> int:
    """Recursive gcd (Euclid)."""
    return abs(a) if b == 0 else gcd_rec(b, a % b)


def sum_digits_rec(n: int) -> int:
    """Recursive sum of digits of |n|."""
    n = abs(n)
    if n < 10:
        return n
    return n % 10 + sum_digits_rec(n // 10)


def is_prime_rec(n: int, d: int = 2) -> bool:
    """Recursive prime test using trial division."""
    if n < 2:
        return False
    if d * d > n:
        return True
    if n % d == 0:
        return False
    # skip even divisors after 2
    return is_prime_rec(n, d + 1 if d == 2 else d + 2)


def count_char_rec(s: str, ch: str) -> int:
    """Count occurrences of ch in s recursively."""
    if not s:
        return 0
    return (1 if s[0] == ch else 0) + count_char_rec(s[1:], ch)


# -------------------------------------------------------------
# 12) Primes at Prime Indices
# -------------------------------------------------------------

def primes_galore(L: list[int]) -> int:
    """Return count of elements in L that are prime and located at prime indices (0-based)."""
    cnt = 0
    for i, val in enumerate(L):
        if is_prime(i) and is_prime(val):
            cnt += 1
    return cnt


# --------------------------
# Quick sanity tests (commented). Uncomment to try locally.
# --------------------------
if __name__ == '__main__':
    # Basic
    assert is_even_two_digit(28) and not is_even_two_digit(-7)
    assert is_palindrome_number(121) and not is_palindrome_number(-123)

    # String
    assert domain_endswith('OpenAI.com')
    assert surround_2_2('abcdef') == '[ab]cd[ef]'
    assert is_pangram('The quick brown fox jumps over a lazy dog')
    assert count_vowels_consonants('abcXYZ') == (1, 5)

    # Lists
    assert second_largest([2, 4, 4, 9, 1]) == 4
    assert is_list_palindrome([1, 2, 1])
    assert merge_sorted([1, 3, 5], [2, 4, 6]) == [1, 2, 3, 4, 5, 6]

    # Counting
    assert count_odd_three_digit([None, -135, 200, 777]) == 2
    assert count_perfect_squares([0, 1, 2, 3, 4, 9, 10]) == 4
    assert count_names_start_with_vowel(['Alice', 'bob', 'Eve', '']) == 2

    # I/O formatting
    assert name_to_initials('John Ronald Reuel Tolkien') == 'J. R. R. Tolkien'

    # Math
    assert sum_floored_to_nearest_10(14, 7) == 20
    assert product_of_digits(1234) == 24
    assert decimal_to_binary(10) == '1010'
    assert digital_root(9999) == 9

    # Matrices
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    C = [[9, 1], [2, 3]]
    assert mat_sum(A, B, C) == [[15, 9], [12, 15]]
    # Product sanity (not asserting exact numeric here).

    # Recursion
    assert sorted(permutations_str('ab')) == ['ab', 'ba']
    assert gcd_rec(12, 18) == 6
    assert sum_digits_rec(9876) == 30
    assert is_prime_rec(17) and not is_prime_rec(10)
    assert count_char_rec('hello world', 'l') == 3

    # Primes at prime indices
    L = [1, 3, 11, 18, 17, 23, 6, 8, 10]
    assert primes_galore(L) == 2

    print('All sanity tests passed!')
