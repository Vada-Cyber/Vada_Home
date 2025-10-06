import datetime

temperatures_list = [-10, -7, -3, 0, 1, 5,8,10, 15, 30]


sum_temps = 0
avg_temps = 0
start_date = datetime.date(2025, 9, 23)


for i, temp in enumerate (temperatures_list):
    print (f" {start_date.strftime('%A')} : {temp}")
    start_date += datetime.timedelta(days=1)
   
# sum_temps = sum(temperatures_list)
    sum_temps += temp
    avg_temps = sum_temps / len(temperatures_list)
print(f"summer is {sum_temps}")
print(f"average is {avg_temps}")
min = min(temperatures_list)
max  = max(temperatures_list)
print (f"minimum is : {min}")
print(f"maximum is : {max}")

