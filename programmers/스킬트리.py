def solution(skill, skill_trees):
    answer = 0
    for skill_tree in skill_trees:
        pivot = 0
        answer += 1
        for i in skill:
            if skill_tree.find(i) != -1 and pivot == -1:
                answer -= 1
                break
            elif pivot > skill_tree.find(i) > -1:
                answer -= 1
                break
            else:
                pivot = skill_tree.find(i)

    return answer