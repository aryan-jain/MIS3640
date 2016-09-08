print('Hello, World!') #single input print command
print('Hey Jude', 'don\'t mkae it bad') #\' allows the user to print an apostrophe even within string quotes
print ('The total number of overall medals in Rio 2016 is', 46 + 37 + 38) #multiple input print command

#Ask for user input
message1 = 'Please enter your first name: '
first_name = input(message1)
message2 = 'Please enter your last name: '
last_name = input(message2)
#print('Hello,', first_name + ' ' + last_name)
age = 2016-1995

# '%' provides a placeholder for multiple entries.
#print('Hello, %s %s. You are now %d years old' % ('Aryan', 'Jain', 21))
print('Hello, %s %s. You are now %d years old' % (first_name, last_name, age))

'Today is %2d-%02d.' % (9, 6) #%2d adds an extra space before the 9, #02d adds an extra space and a '0' before the 6.
'Pi equals %.2f.' % 3.1415926 #%.2f limits the float to 2 decimal places
'Growth rate: %d %%' % 7 #%% allows the user to actually have a '%' in the output.


input()