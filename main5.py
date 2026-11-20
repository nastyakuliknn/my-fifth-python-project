pos = input()
cols = "abcdefgh"

b_col = cols.index(pos[0])
b_row = 8 - int(pos[1])

for r in range(8):
    row_cells = []
    for c in range(8):
        if r == b_row and c == b_col:
            row_cells.append("B")
        elif abs(r - b_row) == abs(c - b_col):
            row_cells.append("*")
        else:
            row_cells.append(".")
    print(" ".join(row_cells))

