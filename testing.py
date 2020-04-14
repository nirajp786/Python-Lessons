import time

with open("test.txt", "a+") as file:
    file.seek(0)
    content = file.read()
    print(content)
    time.sleep(2)
    for x in range(2):
        file.write(content)
listu = [1,2,3,4,5]
listu.reverse()
print(listu)