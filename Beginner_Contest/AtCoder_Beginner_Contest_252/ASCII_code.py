N = int(input())

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

count = 97
for a in alphabet:
    if count == N:
        print(a)
        break
    count+=1