from sys import maxsize
def solution(s):
    def split_char(string, divide_by):
        if string[:divide_by + 1] != string[divide_by+1 : divide_by * 2 + 1]:
            return maxsize
        else:
            new_string = ""
            while (divide_by * 2 + 1) <= len(string):

    answer = 0
    return answer