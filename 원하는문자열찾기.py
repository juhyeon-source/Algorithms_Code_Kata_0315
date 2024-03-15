def solution(myString, pat):
    A = myString.lower()
    B = pat.lower()
    if B in A:
        answer = 1
    else:
        answer = 0
    return answer