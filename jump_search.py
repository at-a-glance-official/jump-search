def jump_search(arr,element):
    jump_size = round(len(arr)**(1/2))
    current = 0

    while arr[current] < element:
        if current + jump_size > len(arr) - 1:
            current = len(arr) - 1
        else:
            current += jump_size
    
    for i in range(current,current-jump_size,-1):
        if element == arr[i]:
            return f'Element found at index {i}'
    return 'Element not found!'

arr = [10,20,54,100,1000,5400]
print(jump_search(arr,545))