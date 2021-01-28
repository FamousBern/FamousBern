# WRITE YOUR CODE SOLUTION HERE

from datetime import datetime

# Get todays date
date = datetime.now().date()

# Get todays day in short form
day = date.strftime('%a')

# The if statement

if day == 'Mon':
    fare = 100
    print('Date:'+str(date)+'\n'+ 'Day:'+day + '\n' +'Fare'+str(fare))

elif day == 'Tue':
    fare = 100
    print('Date:'+str(date)+'\n'+ 'Day:'+day + '\n' +'Fare'+str(fare))

elif day == 'Wed':
    fare = 100
    print('Date:'+str(date)+'\n'+ 'Day:'+day + '\n' +'Fare'+str(fare))

elif day == 'Thu':
    fare = 100
    print('Date:'+str(date)+'\n'+ 'Day:'+day + '\n' +'Fare:'+str(fare))

elif day == 'Fri':
    fare = 100
    print('Date:'+str(date)+'\n'+ 'Day:'+day + '\n' +'Fare'+str(fare))

elif day == 'Sat':
    fare == 60
    print('Date:'+str(date)+'\n'+ 'Day:'+day + '\n' +'Fare'+str(fare))

elif day == 'Sun':
    fare = 80
    print('Date:'+str(date)+'\n'+ 'Day:'+day + '\n' +'Fare'+str(fare))

else:
    print('Done')
        
