import random



kysymys = input ('anna kysymys: ')
sanat = kysymys.split()
print (kysymys)
if sanat[0] == 'montako':
    vastaus = random.randint(1,1000)
    print(vastaus)
    




#sanat ovat splitattu versio kysymyksestä