numbers = [0, -1, -4, 9, 4, 1, -9, 0]

count = 0
count_j = 0
for i in range(len(numbers)):
    rhs = ""
    count_j += 1
    for j in range(i+1, len(numbers)):
        if len(rhs) > 0:
            rhs += ' ,'
        rhs += str(numbers[j])
        if numbers[i] + numbers[j] == 0:
            count+=1
    print(f'{numbers[i]}: {rhs}')
            
#print (f"{count} pairs add up to zero")
print (f"count_j: {count_j}")