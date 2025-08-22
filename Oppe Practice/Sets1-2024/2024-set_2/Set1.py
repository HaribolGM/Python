n = int(input())
for i in range(n):
    left = '\\'
    right = '/'
    spaces_between = 2 * (n - i) - 1
    print(' ' * i + left + ' ' * spaces_between + right)
print(' ' * n + 'x')
for i in range(n-1, -1, -1):
    left = '/'
    right = '\\'
    spaces_between = 2 * (n - i) - 1
    print(' ' * i + left + ' ' * spaces_between + right)