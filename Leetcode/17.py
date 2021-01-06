def letterCombinatinons(digits):
    str_dict = {
        2: "abc",
        3: "def",
        4: "ghi",
        5: "jkl",
        6: "mno",
        7: "pqrs",
        8: "tuv",
        9: "wxyz"
    }

    def add(words, append):
        added_list = []
        for word in words:
            for letter in append:
                added_list.append(word + letter)
        return added_list


    if digits == "":
        return []

    elif len(digits) == 1:
        return list(str_dict[int(digits)])

    else:
        words = list(str_dict[int(digits[0])])
        for i in range(1, len(digits)):
            words = add(words, str_dict[int(digits[i])])


    return words


print(letterCombinatinons("23"))