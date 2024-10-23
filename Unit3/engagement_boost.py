def engagement_boost(engagements):
    # squared_engagements = [] 
    # for i in range(len(engagements)):
    #     squared_engagement = engagements[i] * engagements[i]
    #     squared_engagements.append((squared_engagement, i))
    # squared_engagements.sort(reverse=True)
    # result = [0] * len(engagements)
    # position = len(engagements) - 1
    # for square, original_index in squared_engagements:
    #     result[position] = square
    #     position -= 1
    # return result
    
    squared = [0] * len(engagements) #preallocate the space since its the same length 
    pos = len(engagements)-1
    begin = 0
    end = len(engagements)-1
    while begin <= end:
        left_square = engagements[begin]**2
        right_square = engagements[end]**2
        
        if left_square > right_square:
            squared[pos] = left_square
            begin+=1
        else:
            squared[pos] = right_square
            end-=1
        
        pos-=1
    return squared

print(engagement_boost([-4, -1, 0, 3, 10]))
print(engagement_boost([-7, -3, 2, 3, 11]))
#[0, 1, 9, 16, 100]
#[4, 9, 9, 49, 121]