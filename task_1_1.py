number=int(input('Duration: '))
seconds=number%60
minutes=number//60%60
hours=number//3600%24
days=number//24//60//60%60
if number<60:
    print(seconds, 'сек')
elif 60<number<3600:
    print(minutes, 'мин', seconds, 'сек')
elif 3600<number<86400:
    print(hours, 'час', minutes, 'мин', seconds, 'сек')
else:
    print(days,'дн', hours, 'час', minutes, 'мин', seconds, 'сек')
