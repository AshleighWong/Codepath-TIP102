def reverse_watchlist(watchlist):
    begin = 0
    end = len(watchlist) - 1
    
    while begin < end:
        watchlist[begin], watchlist[end] = watchlist[end], watchlist[begin]
        begin +=1
        end-=1
    
    return watchlist



lists = ["Breaking Bad", "Stranger Things", 'poop', "The Crown", "The Witcher"]
print(reverse_watchlist(lists))  