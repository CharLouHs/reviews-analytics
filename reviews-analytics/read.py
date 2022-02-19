data=[]
count=0
k=0
with open('../reviews.txt','r') as f:
    for line in f:
        data.append(line)
        k+=len(line)
        count += 1
        if count % 1000==0:
            print(len(data))
print('檔案讀取完，共有',len(data),'筆資料')
avg= k/len(data)
print('平均長度為: ',avg ,' 個字')
print(data[0])

new=[]
for d in data:
    if len(d)<100:
        new.append(d)
print('一共有',len(new),'筆留言長度小於100')

good = []
for d in data:
    if 'good' in d:
        good.append(d)
print('有good的留言有: ',len(good),'筆')
dd=[d for d in data]
print(dd)

good = [d for d in data if 'good' in d] #good是一個清單  第一個d就是上面的append(d)

bad=['bad' in d for d in data] #1000000筆d 每一筆列出是true  / false
bad = []
for d in data:
    bad.append('bad' in d)
