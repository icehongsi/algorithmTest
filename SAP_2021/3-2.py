while True:
    n = int(input())
    if n == 0:
        break
    bin_list = ["?"] * 32
    for i in range(n):
        order = input().split(" ")
        order[1] = 31 - int(order[1])
        if len(order) == 3:
            order[2] = 31 - int(order[2])
        if order[0] == "SET":
            bin_list[order[1]] = "1"
        elif order[0] == "CLEAR":
            bin_list[order[1]] = "0"
        elif order[0] == "AND":
            if bin_list[order[1]] == "?" or bin_list[order[2]] == "?":
                bin_list[order[1]] = "?"
            else:
                bin_list[order[1]] = bin_list[order[1]] and bin_list[order[2]]
        elif order[0] == "OR":
            if bin_list[order[1]] == "0" or bin_list[order[2]] == "0":
                if bin_list[order[1]] == "?" or bin_list[order[2]] == "?":
                    bin_list[order[1]] = "?"
                else:
                    bin_list[order[1]] = bin_list[order[1]] or bin_list[order[2]]
            elif bin_list[order[1]] == "1" or bin_list[order[2]] == "1":
                bin_list[order[1]] = "1"
        print("".join(bin_list))
