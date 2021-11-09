def solution(genres, plays):
    answer = []
    dic = {}
    play_sum = {}
    for i in range(len(genres)):
        if genres[i] not in dic:
            dic[genres[i]] = [[i, plays[i]]]
            play_sum[genres[i]] = plays[i]
        else:
            dic[genres[i]].append([i, plays[i]])
            play_sum[genres[i]] += plays[i]
    for _, val in dic.items():
        val.sort(key=lambda x: x[1], reverse=True)
    for key, val in sorted(play_sum.items(), key=lambda x: x[1], reverse=True):
        if len(dic[key]) < 2:
            answer.append(dic[key][0][0])
        else:
            answer += [dic[key][0][0], dic[key][1][0]]
    return answer