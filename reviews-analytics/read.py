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
print('平均長度為: ',avg ,'個字')
print(data[0])
