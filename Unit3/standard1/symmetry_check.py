#can also use dequeue to check for symmetry
#this uses two pointers
def is_symmetrical_title(title):
    title = title.lower().replace(' ', '')
    left = 0
    right = len(title) -1
    while left < right:
       if title[left] != title[right]:
         return False
       left +=1
       right -=1
    return True


print(is_symmetrical_title("A Santa at NASA"))
print(is_symmetrical_title("Social Media")) 