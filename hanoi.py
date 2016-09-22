def hanoi(n, source, bridge, destination):
    if n >= 1:
        hanoi(n-1, source, destination, bridge)
        print(source, ' --> ', destination)
        hanoi(n-1, destination, bridge, source)
        
hanoi(3,'A','B','C')