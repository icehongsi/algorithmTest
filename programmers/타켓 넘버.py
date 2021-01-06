def solution(numbers, target):
    global result
    result = 0

    def find(index, value):
        global result
        print(index, value)
        if index == len(numbers):
            if target == value:
                result += 1
            return

        find(index + 1, value + numbers[index])
        find(index + 1, value - numbers[index])

    find(1, numbers[0])
    find(1, -numbers[0])

    return result

print(solution([1, 1, 1, 1, 1], 3))