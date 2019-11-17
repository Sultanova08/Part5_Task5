def solution(A, B):
    list_of_alive_fish = []
    alive =0
    for index in range(len(A)):
        if B[index] == 0:
            if list_of_alive_fish == []:
                alive += 1
            elif list_of_alive_fish[-1] > A[index]:
                continue
            else:
                active = True
                while active:
                    list_of_alive_fish.pop()
                    if list_of_alive_fish == []:
                        alive += 1
                        active = False
                    elif list_of_alive_fish[-1] > A[index]:
                        active = False

        if B[index] == 1:
            list_of_alive_fish.append(A[index])

    res = len(list_of_alive_fish) + alive
    return res