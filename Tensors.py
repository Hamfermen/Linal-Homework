# Задание 10

a = [[[[-5, -1], [-6, 0]],
      [[-3, 5], [2, -4]]],
     [[[3, 4], [1, -3]],
    [[1, -4], [1, 4]]]]

v = [[1, 5], [-6, -3]]
u = [[1, -3], [4, 3]]

s = 0

for j in range(2):
    for k in range(2):
        for l in range(2):
            s += v[0][j] * v[1][k] * u[0][l] * (u[1][0] * a[l][0][j][k] + u[1][1] * a[l][1][j][k])
print(s)

# Задание 11

a = [[[[0 for x in range(3)] for y in range(3)] for z in range(3)] for w in range(3)]

for i in range(3):
    for j in range(3):
        for k in range(3):
            for l in range(3):
                a[i][j][k][l] = 2*i-2*j+k-l

for i in range(3):
    for j in range(3):
        print(end=";")
        for k in range(3):
            for l in range(3):
                print(a[j][l][k][i], end=", ")
                
# Задания с симмитризацией
a = [[[[[0 for x in range(2)] for y in range(2)] for z in range(2)] for w in range(2)] for v in range(2)]

inp = list(map(int, input().split()))

ind = 0

for n in range(2):
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    a[l][j][i][k][n] = inp[ind]
                    ind += 1

b = [[[[[0 for x in range(2)] for y in range(2)] for z in range(2)] for w in range(2)] for v in range(2)]

for n in range(2):
    for i in range(2):
        for j in range(2):
            for k in range(2):
                for l in range(2):

                    # Задание 2

                    b[l][k][j][i][n] = (a[l][k][j][i][n] + a[l][k][j][n][i] +
                                        a[l][k][i][j][n] + a[l][k][i][n][j] +
                                        a[l][k][n][j][i] + a[l][k][n][i][j] +

                                        a[j][k][l][i][n] + a[j][k][l][n][i] +
                                        a[j][k][i][l][n] + a[j][k][i][n][l] +
                                        a[j][k][n][l][i] + a[j][k][n][i][l] +

                                        a[i][k][j][l][n] + a[i][k][j][n][l] +
                                        a[i][k][l][j][n] + a[i][k][l][n][j] +
                                        a[i][k][n][j][l] + a[i][k][n][l][j] +

                                        a[n][k][j][i][l] + a[n][k][j][l][i] +
                                        a[n][k][i][j][l] + a[n][k][i][l][j] +
                                        a[n][k][l][j][i] + a[n][k][l][i][j]
                                        ) * (1/24)
                    # b[l][j][i][k][n] = (a[l][j][i][k][n] + a[j][l][i][k][n]) * (1/2) для задания 3

                    # b[l][j][i][k][n] = (a[l][j][i][k][n] + a[i][j][l][k][n]) * (1/2) для задания 1


for n in range(2):
    for i in range(2):
        print(end=";")
        for j in range(2):
            for k in range(2):
                for l in range(2):
                    print(round(b[i][l][k][n][j], 2), end=", ")

