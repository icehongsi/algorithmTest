









def solution():
    binaryTree = []
    while True:
        temp = input()
        if not temp:
            break
        binaryTree.append(int(temp))

    postorder = []
    def search(start, end):
        if start > end:
            return

        temp = start + 1
        while temp < len(binaryTree) and binaryTree[temp] < binaryTree[start]:
            temp += 1

        search(start + 1, temp - 1) #L Subtree에 대한 순회
        search(temp, end) #R Subtree에 대한 순회

        postorder.append(binaryTree[start])

    search(0, len(binaryTree) - 1)

    print(postorder)

solution()