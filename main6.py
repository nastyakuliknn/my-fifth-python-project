pos = input()
cols = "abcdefgh"

r_col = cols.index(pos[0])
r_row = 8 - int(pos[1])

for r in range(8):
    row_cells = []
    for c in range(8):
        if r == r_row and c == r_col:
            row_cells.append("R")
        elif r == r_row or c == r_col:
            row_cells.append("*")
        else:
            row_cells.append(".")
    print(" ".join(row_cells))

