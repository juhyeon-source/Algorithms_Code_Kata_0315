# 딕셔너리로 푼 방법
def solution(rsp):
    answer = ''
    dic = {'2':'0', '0':'5', '5':'2'}
    for i in rsp:
        answer += dic[i]
    return answer

# 리스트로 푼 방법
def solution(rsp):
    answer = []
    for i in rsp:
        if i == '2':
            answer.append('0')
        if i == '0':
            answer.append('5')
        if i == '5':
            answer.append('2')
    return ''.join(answer)