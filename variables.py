# # f = open("variable.txt", "w")
# # f.write("ahem")
# # f.close()


# from datetime import datetime
# import time


# f = open("variable.txt", "r")
# def dereferentie():
#     aaa = f.read()
#     checkMinute(aaa)

# def checkMinute(aaa):

#     #if currentMinute has changed do:
#         printSomething()

# def printSomething():
#     print (f.read())


# def main():
#     while (1):
#         dereferentie()


# if __name__ == '__main__':
#     main()


# # while True:
# #     f = open("variable.txt", "r")
# #     aaa = f.read()
# #     f.seek(0)
# #     print(aaa)
# #     while True:
# #         if f.read() != aaa:
# #             break
# f = open("variable.txt", "r")
# i = 0


# # print (f.read())

# # aaa = f.read()
# # print (aaa)

# while i < 5 :
#     i = i+1
#     aaa = f.read()
#     f.seek(0)
#     print(f.read())
#     print(aaa)

# import requests

# f = open("variable.txt", "r")
# def getIP():
#     while True:
#         try:
#              aaa = f.read()
#              print(aaa)
#         except KeyboardInterrupt:
#              print("\nProccess terminated by user")
#     return aaa

def client():
    while True:
        f = open("variable.txt", "r")
        f.seek(0)
        if f.read() != "0":
            break
    f = open("variable.txt", "r+")
    print(f.read())
    f.seek(0)
    query = (f.read())
    f.seek(0)
    f.truncate()
    f.write("0")
    f.close()



while True:
    f = open("variable.txt", "r+")
    print(f.read())
    f.seek(0)
    query = (f.read())
    f.seek(0)
    f.truncate()
    f.write("0")
    f.close()
    if query == "how are you":
        print("Fine, How Are You Sir?")
        while True:
            f = open("variable.txt", "r")
            f.seek(0)
            if f.read() != "0":
                break
        f = open("variable.txt", "r+")
        print(f.read())
        f.seek(0)
        query = (f.read())
        f.seek(0)
        f.truncate()
        f.write("0")
        f.close()
        if query == "good":
            print("cool")
        elif query == "not good":
            print("sorry")
    print("Command Received")
    while True:
        f = open("variable.txt", "r")
        f.seek(0)
        if f.read() != "0":
            break
