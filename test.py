f = open('badwords.txt', 'r',encoding = "utf-8")
ff = f.readlines()

user = 'abcd'.lower() 
for i in ff: 
    if user.find(i.strip()) >= 0:
        user = '금지어' 
        break


print(user)

