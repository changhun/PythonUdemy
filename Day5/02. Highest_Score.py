
# 문자열이 ', ' 로 나뉘어 있는지 ' ' 로 나뉘어 있는지 모를 때 어떻게 파싱하지?
scores = input("Input student's scores  ").split(", ")
# for score in scores:
#     score = int(score)

for i in range(0, len(scores)):
    scores[i] = int(scores[i])

max_value = 0
for score in scores:
    if score > max_value:
        max_value = score

print(max_value)