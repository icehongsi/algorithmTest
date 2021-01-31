import re
def solution(new_id):
    new_id = str(re.sub('[^a-z0-9\-._]', '', new_id.lower()))
    while ".." in new_id:
        new_id = new_id.replace("..", ".")
    while new_id != '' and new_id[0] == ".":
        new_id = new_id[1:]
    while new_id != '' and new_id[-1] == ".":
        new_id = new_id[:len(new_id) - 1]
    if not new_id:
        new_id = "a"
    if len(new_id) > 15:
        new_id = new_id[:14] + new_id[14].replace(".", "")
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id


print(solution("=.="))



import re

def solution(new_id):
    st = new_id
    st = st.lower() #1
    st = re.sub('[^a-z0-9\-_.]', '', st) #2
    st = re.sub('\.+', '.', st) #3
    st = re.sub('^[.]|[.]$', '', st) #4
    st = 'a' if len(st) == 0 else st[:15] #5
    st = re.sub('^[.]|[.]$', '', st) #6
    st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))]) #7
    return st

#http://www.codejs.co.kr/%EC%A0%95%EA%B7%9C%EC%8B%9D-regular-expression/