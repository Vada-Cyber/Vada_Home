""" status should "hot" after 35 degrees and "not hot" under it  """

# #temp = 39
# status = "status"

# if temp < 30:
#     # code block, and 4 space is "indentation"
#     status = "Not_Hot"
# elif 30 < temp  and  temp < 40 :
#     status = "good"
# else :
#     print(f"status: {status}")

temp = 11
status = "status"

if temp < 16:
    # code block, and 4 space is "indentation"
    status = "It's_cold"
elif 16 >= temp  and  temp <= 21:
    status = "It's_good"
else :
    status = "It's_hot"
print(f"status: {status}") 
