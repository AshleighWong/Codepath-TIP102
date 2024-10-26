
def apply_rating_operations(ratings):
    for i in range(len(ratings) - 1):
        if ratings[i] == ratings[i+1]:
            ratings[i] *=2
            ratings[i+1] = 0
        
    final = [n for n in ratings if n !=0]
    
    final += ([0] * (len(ratings)-len(final)))
    return final
    
    
print(apply_rating_operations([1, 2, 2, 1, 1, 0])) 
print(apply_rating_operations([0, 1])) 