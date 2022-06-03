import sys

# argv[0] nome programma ... gli altri i valori da console
if __name__ == "__main__":
    n_1 = int(sys.argv[1])
    n_2 = int(sys.argv[2])
    op = str(sys.agrv[3])
    if op == "add":
        print(f"operazione {n_1} + {n_2} = ", n_1 + n_2)
    elif op == "mol":
        print(f"operazione {n_1} * {n_2} = ", n_1 * n_2)
    elif op == "sub":
        print(f"operazione {n_1} - {n_2} = ", n_1 - n_2)
    else:
        print(f"operazione {n_1} / {n_2} = ", n_1 / n_2)
