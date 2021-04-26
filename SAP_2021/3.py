while True:
    n = int(input())
    if n == 0:
        break
    bin_list = ["?"] * 32
    for i in range(n):
        test = input().split()
        if test[0] == "CLEAR":
            bin_list[int(test[1])] = "0"
        elif test[0] == "SET":
            bin_list[int(test[1])] = "1"
        elif test[0] == "AND":
            a, b = int(test[1]), int(test[2])
            if bin_list[a] == '1' and bin_list[b] == "1":
                bin_list[a] = "1"
            elif bin_list[a] == "0" or bin_list[b] == "0":
                bin_list[a] = "0"
            else:
                bin_list[a] = "?"
        else:
            a, b = int(test[1]), int(test[2])
            if bin_list[a] == "1" or bin_list[b] == "1":
                bin_list[a] = "1"
            elif bin_list[a] == "0" and bin_list[b] == "0":
                bin_list[a] = "0"
            else:
                bin_list[a] = "?"

        print("".join(bin_list)[::-1])