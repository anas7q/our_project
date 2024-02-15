num=int(input("enter number whent to know reprted"))
count=0
i=1
x=0
while i<num:
  x=num%10
  num=num//10
  if x ==5:
    count+=1
print(count)
'''
Q2B107
stro=input("enter the str to know how vowels :")
vowel="aeiou"
vowel2="AEIOU"
count=0
for i in stro:
  if i in vowel or i in vowel2:
    stro=stro.replace(i,"")
    count+=1
print(count)
print(stro)

'''