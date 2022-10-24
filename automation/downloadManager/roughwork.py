import os

'''list = ["1", "2", "3"]
print(len(list))'''  # this is to see how to count lists. why wont it work for the list i have though?
                     # ohhhhhhhhhhhhhh its because i have string values!!!!!!!

entries = os.listdir('/home/calst/Downloads')
for entry in entries:
    print(entry)
print(len(entries))