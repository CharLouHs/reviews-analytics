import string

ps = string.punctuation

data = []
count = 0
k = 0
with open('./reviews.txt', 'r') as f:
    for line in f:
        data.append(line.strip())

print('檔案讀取完，共有', len(data), '筆資料')
# print(data[0])
words_count = {}
for d in data[0:100]:
    words = d.split(' ')
    for indi in words:
        for i in ps:
            indi = indi.replace(i, '')
        if indi in words_count:

            words_count[indi] += 1
        else:
            words_count[indi] = 1

for word in words_count:
    if words_count[word] > 100:
        print(word, ':', words_count[word])

while True:
    f = input("請輸入要查詢的字")
    if f == 'q':
        print('感謝使用!!!')
        break;
    elif f in words_count:
        print(f, '的出現次數為:', words_count[f], ' 次')
    else:
        print('沒有此字，請重新查詢!!')
