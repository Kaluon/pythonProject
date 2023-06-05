import numpy as np

# Setting the example matrix
matrix = np.array([
    [0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 2, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 2, 1, 0],
    [1, 2, 0, 1, 1, 1, 2, 0, 1, 0, 1, 0, 2, 1, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1]
])

# Calculate prior probabilities and conditional probabilities
def get_Py_Pxy():
    count01 = np.sum(matrix[3])
    count0 = len(matrix[3]) - count01
    Py = np.array([(count0 + 1) / (len(matrix[3]) + 2), (count01 + 1) / (len(matrix[3]) + 2)])

    px1 = np.zeros((4, 2), dtype=np.float64)
    px2 = np.zeros((6, 2), dtype=np.float64)
    px3 = np.zeros((6, 2), dtype=np.float64)

    for i in range(len(matrix[0])):
        x1 = matrix[0][i]
        x2 = matrix[1][i]
        x3 = matrix[2][i]
        y = matrix[3][i]

        px1[x1][y] += 1
        px2[x2][y] += 1
        px3[x3][y] += 1

    px1[:, 0] = (px1[:, 0] + 1) / (count0 + 2)
    px1[:, 1] = (px1[:, 1] + 1) / (count01 + 2)
    px2[:, 0] = (px2[:, 0] + 1) / (count0 + 3)
    px2[:, 1] = (px2[:, 1] + 1) / (count01 + 3)
    px3[:, 0] = (px3[:, 0] + 1) / (count0 + 3)
    px3[:, 1] = (px3[:, 1] + 1) / (count01 + 3)

    print("---------------Prior Probabilities---------------")
    print("P(y = 0) =", Py[0])
    print("P(y = 1) =", Py[1])
    print()

    print("---------------Conditional Probabilities---------------")
    print("P(x1 | y):")
    for i in range(4):
        print("P({} | 0) =".format(i), px1[i][0])
        print("P({} | 1) =".format(i), px1[i][1])
    print()

    print("P(x2 | y):")
    for i in range(6):
        print("P({} | 0) =".format(i), px2[i][0])
        print("P({} | 1) =".format(i), px2[i][1])
    print()

    print("P(x3 | y):")
    for i in range(6):
        print("P({} | 0) =".format(i), px3[i][0])
        print("P({} | 1) =".format(i), px3[i][1])
    print()

    return Py, px1, px2, px3

# Classify the given sample 's'
def s_classify(s, Py, px1, px2, px3):
    p0 = Py[0]
    p1 = Py[1]

    p0 *= px1[s[0]][0] * px2[s[1]][0] * px3[s[2]][0]
    p1 *= px1[s[0]][1] * px2[s[1]][1] * px3[s[2]][1]

    print("---------------Posterior Probabilities---------------")
    print("P(y = 0) =", p0)
    print("P(y = 1) =", p1)
    print()

    if p1 >= p0:
        return 1
    return 0

# Main function
def main():
    print("This is the Bayesian classifier:")
    print("Let gender be {female, male} = {0, 1}")
    print("Let age range be {10-20, 20-40, >40} = {0, 1, 2}")
    print("Let preferred genre be {martial arts, sci-fi, history} = {0, 1, 2}")
    print("Let purchase decision be {yes, no} = {1, 0}")
    print()

    Py, px1, px2, px3 = get_Py_Pxy()

    s = [0, 0, 0]
    print("Please enter 3 integers to classify the sample: ")
    s[0], s[1], s[2] = map(int, input().split())

    if s_classify(s, Py, px1, px2, px3):
        print("The sample belongs to class 1")
        print("The customer is likely to purchase the book.")
    else:
        print("The sample belongs to class 0")
        print("The customer is unlikely to purchase the book.")

if __name__ == '__main__':
    main()
