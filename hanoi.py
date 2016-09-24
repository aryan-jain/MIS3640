'''
def hanoi(n, source, bridge, destination):
    if n >= 1:
        hanoi(n-1, source, destination, bridge)
        print(source, ' --> ', destination)
        hanoi(n-1, destination, bridge, source)
        
hanoi(3,'A','B','C')
'''

def hanoi(n, source, bridge, destination):
    if n==1:
        print(source, ' --> ', destination)
    else: 
        hanoi(n-1, source, destination, bridge)
        print(source, ' --> ', bridge)

hanoi(3,'A','B','C')