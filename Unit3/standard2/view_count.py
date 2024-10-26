def minimum_average_view_count(view_counts):
    view_counts.sort()
    begin = 0
    end = len(view_counts)-1
    min_avg = float('inf')
    
    while begin < end:
        avg_view = (view_counts[begin] + view_counts[end]) / 2
        min_avg = min(min_avg, avg_view)
        begin +=1
        end-=1
    
    return min_avg

print(minimum_average_view_count([7, 8, 3, 4, 15, 13, 4, 1])) 
print(minimum_average_view_count([1, 9, 8, 3, 10, 5])) 
print(minimum_average_view_count([1, 2, 3, 7, 8, 9])) 