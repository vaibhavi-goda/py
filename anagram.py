str1=input("Enter first string")
str2=input("Enter second string")
print(sorted(str1))
print(sorted(str2))
if(sorted(str1)==sorted(str2)):
    print("Anagrams")
else:
    print("Not Anagrams")
