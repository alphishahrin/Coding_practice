#      *
#     * *
#    *   *
#   *     *
#  *       *
# ***********

# space n-i-1 and star 2n + 1 (n=0 or n=5)
# space n-i-1 and star and space 2n - 1 and star


n = int(input())

for i in range(n):
    if i==0 or i==n-1:
        print(' ' * (n-i - 1) + '*' * (2*i + 1))
    else:
        print(' ' * (n-i - 1) + '*' + ' ' * (2 * i - 1) + '*')

