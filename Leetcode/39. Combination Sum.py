def combination_pair(candidates, target):
    result = []
    def select(candidate, current_sum, selected):
        if current_sum == 0 and sorted(selected) not in result:
            result.append(sorted(selected))
            return
        for i in candidate:
            if current_sum - i >= 0:
                select(candidate, current_sum - i, selected + [i])
            else:
                return


    select(sorted(candidates), target, [])
    return result


combination_pair([2,3,6,7], 7)
combination_pair([2,3,5],8)

#answer

def combination_pair(candidates, target):
    result = []
    def dfs(remained, index, elem):
        if remained < 0:
            return
        if remained == 0:
            result.append(elem)
            return
        for i in range(index, len(candidates)):
            dfs(remained - candidates[i], i, elem + [candidates[i]])

    dfs(target, 0, [])
    print(result)
    return result



combination_pair([2,3,6,7], 7)
combination_pair([2,3,5],8)

#revised

def combination_pair(candidates, target):
    result = []
    def select(current_sum, index, selected):
        if current_sum < 0:
            return
        if current_sum == 0:
            result.append(selected)
            return
        for i in range(index, len(candidates)):
            select(current_sum - candidates[i], i, selected + [candidates[i]])

    select(target, 0, [])
    return result

combination_pair([2,3,6,7], 7)
combination_pair([2,3,5],8)