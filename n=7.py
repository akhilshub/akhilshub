L = [90, 47, 8, 18, 10, 7]
S = [L[0]]	# list containing just one element
for i in range(1, len(L)):
    flag = True
    for j in range(len(S)):
        if L[i] < S[j]:
            before_j = S[: j]	# elements in S before index j
            new_j = [L[i]]		# list containing just one element
            after_j = S[j: ]	# elements in S starting from index j
            # what is the size of S now?
            S = before_j + new_j + after_j
            # what is the size of S now?
            flag = False
            break
    if flag:
        S.append(L[i])
print(S)