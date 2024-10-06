"""
This is a simple program to get spiral traversal of matrix elements
Example
if their exist a Matrix of dimension 3x3 i.e, 3 rows and 3 columns like below

1 2 3
4 5 6
7 8 9

then the spiral traversal will be
1 2 3 6 9 8 7 4 5

Example output 1:

ENTER THE NUMBER OF ROWS: 3
ENTER THE NUMBER OF COLUMNS: 3
ENTER 1st row 1st column element: 1
ENTER 1st row 2nd column element: 2
ENTER 1st row 3rd column element: 3
ENTER 2nd row 1st column element: 4
ENTER 2nd row 2nd column element: 5
ENTER 2nd row 3rd column element: 6
ENTER 3rd row 1st column element: 7
ENTER 3rd row 2nd column element: 8
ENTER 3rd row 3rd column element: 9
YOUR ENTERED MATRIX
1 2 3
4 5 6
7 8 9
REQUIRED OUTPUT/RESULT
[1, 2, 3, 6, 9, 8, 7, 4, 5]

Example output 2:

ENTER THE NUMBER OF ROWS: 3
ENTER THE NUMBER OF COLUMNS: 2
ENTER 1st row 1st column element: 10
ENTER 1st row 2nd column element: 5
ENTER 2nd row 1st column element: 4
ENTER 2nd row 2nd column element: 2
ENTER 3rd row 1st column element: 1
ENTER 3rd row 2nd column element: 6
YOUR ENTERED MATRIX
10 5
4 2
1 6
REQUIRED OUTPUT/RESULT
[10, 5, 2, 6, 1, 4]

"""

m = 0
n = 0


def inputs():
    try:
        global m
        global n
        m = int(
            input("ENTER THE NUMBER OF ROWS: ")
        )  # In a MxN matrix M represents number of rows
        n = int(
            input("ENTER THE NUMBER OF COLUMNS: ")
        )  # In a MxN matrix N represents number of columns
        return True
    except Exception as e:
        print("ENTER ONLY INTEGER VALUE")
        return False


def spiral_traversal():
    mat = []
    for i in range(m):
        a = []
        if i + 1 == 1:
            row_suffix = "st"
        elif i + 1 == 2:
            row_suffix = "nd"
        elif i + 1 == 3:
            row_suffix = "rd"
        else:
            row_suffix = "th"
        for j in range(n):
            if j + 1 == 1:
                column_suffix = "st"
            elif j + 1 == 2:
                column_suffix = "nd"
            elif j + 1 == 3:
                column_suffix = "rd"
            else:
                column_suffix = "th"
            # to have only int as input need to wrap input() with int() eg: int(input(....)) in the below code
            a.append(
                input(
                    f"ENTER {i+1}{row_suffix} row {j+1}{column_suffix} column element: "
                )
            )
        mat.append(a)

    print("YOUR ENTERED MATRIX")
    for i in range(m):
        for j in range(n):
            print(mat[i][j], end=" ")
        print()

    print("REQUIRED OUTPUT/RESULT")
    toprow = 0
    bottomrow = len(mat) - 1
    left = 0
    right = len(mat[0]) - 1
    direction = 0  # their are 4 direction Top, Right, Bottom, Left so we assigned 0, 1, 2, 3 respectively
    r = []
    while toprow <= bottomrow and left <= right:
        if direction == 0:
            for i in range(left, right + 1):
                r.append(mat[toprow][i])
            toprow = toprow + 1

        if direction == 1:
            for i in range(toprow, bottomrow + 1):
                r.append(mat[i][right])
            right = abs(right - 1)

        if direction == 2:
            for i in range(right, left - 1, -1):
                r.append(mat[bottomrow][i])
            bottomrow = abs(bottomrow - 1)

        if direction == 3:
            for i in range(bottomrow, toprow - 1, -1):
                r.append(mat[i][left])
            left = left + 1

        direction = (direction + 1) % 4

    print(r)


if __name__ == "__main__":
    flag = inputs()
    while not flag:
        flag = inputs()
    spiral_traversal()
