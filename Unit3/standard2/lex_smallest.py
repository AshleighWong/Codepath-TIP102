def make_smallest_watchlist(watchlist):
    watch = list(watchlist)
    begin = 0
    end = len(watch) - 1
    
    while begin < end:
        if watch[begin] != watch[end]:
            if watch[begin] < watch[end]:
                watch[end] = watch[begin]
            watch[begin] = watch[end]
        begin +=1
        end-=1
    return ''.join(watch)

print(make_smallest_watchlist("egcfe")) 
print(make_smallest_watchlist("abcd")) 
print(make_smallest_watchlist("seven")) 