import time

time = time.time()
print(time)
sec = time % 60
min = int(time/60) % 60
hour = int((time/60)/60) % 24
days = int(((time/60)/60)/24)

print('It has been %d days, %d hours, %d minutes and %d seconds since epoch.' % (days, hour, min, sec))