# ABCDEDCBA
# ABCD DCBA
# ABC   CBA
# AB     BA 
# A       A 
# AB     BA 
# ABC   CBA
# ABCD DCBA
# ABCDEDCBA 

N=8
Ascii_val = 65

for i in range(2*N - 1):
    if i==0:
        for j in range(0, N-i):
            print(chr(Ascii_val+j), end='')
        for j in range(N-i-2, -1, -1):
            print(chr(Ascii_val+j), end='')
    if i>0 and i < N:
        for j in range(0, N-i):
            print(chr(Ascii_val+j), end='')
        print('_'*(2*i - 1), end='')
        for j in range(N-i-1, -1, -1):
            print(chr(Ascii_val+j), end='')
    if i>=N and i<(2*N-2):
        for j in range(0, i - N + 2):
            print(chr(Ascii_val + j), end='')
        print('_' * (2 * N - 2 * (i - N + 2) - 1), end='')
        for j in range(i - N + 1, -1, -1):
            print(chr(Ascii_val + j), end='')
    if i==(2*N-2):
        for j in range(0, i - N + 2):
            print(chr(Ascii_val + j), end='')
        for j in range(i - N, -1, -1):
            print(chr(Ascii_val + j), end='')
    print()

