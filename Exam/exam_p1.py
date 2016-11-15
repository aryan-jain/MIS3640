def speak_Chinese(num):
    '''
    number: a integer, 0<=number<99

    Returns: a string that is the number in Chinese
    '''
    chnums = {'0':'ling', '1':'yi', '2':'er', '3':'san', '4':'si', '5':'wu', '6':'liu', '7':'qi', '8':'ba', '9':'jiu', '10':'shi', '100':'bai'}

    if num < 0 or num > 999:
        raise ValueError
    number = str(num)
    if number in chnums.keys():
        if num == 100:
            return 'yi bai'
        else:
            return chnums[number]
    if len(number) == 2:
        if number[0] == '1':
            return chnums['10'] + ' ' + chnums[number[1]]
        elif number[1] == '0':
            return chnums[number[0]] + ' ' + chnums['10']
        else:
            return chnums[number[0]] + ' ' + chnums['10'] + ' ' + chnums[number[1]]
    if len(number) == 3:
        if number[1:] == '00':
            return chnums[number[0]] + ' ' + chnums['100']
        elif number[1] == '0':
            return chnums[number[0]] + ' ' + chnums['100'] + ' ' + chnums['0'] + ' ' + speak_Chinese(int(number[2]))
        else:
            return chnums[number[0]] + ' ' + chnums['100'] + ' ' + speak_Chinese(int(number[1:]))
    return 'ling'
        

# For testing
def main():
    print(speak_Chinese(36))
    print('In Chinese: 36 = san shi liu')
    print(speak_Chinese(20))
    print('In Chinese: 20 = er shi')
    print(speak_Chinese(16))
    print('In Chinese: 16 = shi liu')
    print(speak_Chinese(100))
    print('In Chinese: 100 = yi bai')
    print(speak_Chinese(109))
    print('In Chinese: 109 = yi bai ling jiu')
    print(speak_Chinese(450))
    print('In Chinese: 450 = si bai wu shi')
    print(speak_Chinese(600))
    print('In Chinese: 600 = liu bai')
    print(speak_Chinese(999))
    print('In Chinese: 999 = jiu bai jiu shi jiu')

if __name__ == '__main__':
    main()
