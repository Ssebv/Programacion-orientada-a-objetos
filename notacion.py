# Ley de la suma
def f(n):

    for i in range(n):
        print(i)

    for i in range(n):
        print(i)

# O(n) + O(n) = O(n + n) = O(2n) = O(n)


def f1(n):

    for i in range(n):
        print(i)

    for i in range(n*n):
        print(i)

# O(n) + O(n*n) = O(n+n^2) =  O(n^2)


# Ley de la multiplicacion


def f2(n):

    for i in range(n):
        for j in range(n):
            print(i, j)

# O(n) * O(n) = O(n*n) = O(n^2)
