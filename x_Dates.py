import datetime

x = datetime.datetime.now()
print(x)
print(x.year) #year returned
print(x.strftime("%A")) #returns day of week

# Create an object

y = datetime.datetime(2020, 5, 3)
print(y.strftime("%B")) #returns month


# visit https://www.w3schools.com/python/python_datetime.asp
# or more formatting codes