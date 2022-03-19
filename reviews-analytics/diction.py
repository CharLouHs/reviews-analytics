# dictionary

words = {
    'ramen': '拉麵',
    'pasta': '義大利麵'
}
words['tea']='茶' #增加新的key
print(words)
#print(words['ramen'])
#print(words['pasta'])
#print(words['tea'])

po={
    'name':'麥香奶茶',
    'price':60
}

p1={
    'name':'錫蘭奶茶',
    'price':160
}

drinks=[po,p1]
drinks[0]['name'] #麥香奶茶
drinks[1]['price'] #60
