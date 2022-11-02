with open("code.txt") as file:
    line = file.readlines()

# x = "awesome"
#
# def myfunc():
#   global x
#   x = "fantastic"
#
# myfunc()
#
# print("Python is " + x)


# answer = True
# def biggerDummy():
#
#     print(answer)
#
#     def dummy():
#         global answer
#         answer = False
#
#
#     dummy()
#     print("LINE 15", answer)
#     return answer
#
# print(biggerDummy())



line_str = str(line[0])
new = ["(" if letter == "{" else letter for letter in line_str]
new2 = [")" if letter == "}" else letter for letter in new]
new2 = ["=" if letter == ":" else letter for letter in new2]
answer = ''.join(new2)
print(answer)

f = open(file="answer.txt", mode='w', encoding="utf-8")
f.write(answer)
f.close()