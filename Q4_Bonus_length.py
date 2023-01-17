numbers = [-5, 94, 1001, -100, 76, 0,5, 503]
newArray = []
for i in numbers:
    if len(str(i)) > 1 :
        pass
    else:
        newArray.append(i)

print(max(newArray))