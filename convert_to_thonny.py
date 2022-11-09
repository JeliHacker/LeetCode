import sys

file_name = "/Users/jeligooch/Desktop/git/LeetCode/" + sys.argv[1]

# with open(file_name) as file:
#     line = file.readlines()
#
# line_str = str(line[0])
# new = ["(" if letter == "{" else letter for letter in line_str]
# new2 = [")" if letter == "}" else letter for letter in new]
# new2 = ["=" if letter == ":" else letter for letter in new2]
# answer = ''.join(new2)

with open(file_name) as file:
    filedata = file.read()

    filedata = filedata.replace('List', 'list')
    filedata = filedata.replace('self, ', '')


f = open(file=file_name, mode='w', encoding="utf-8")
f.write(filedata)
f.close()

try:
    if sys.argv[2]:
        print("")
        print("")
        print("___________________COPY BELOW___________________")
        print(filedata)
        print("___________________END OF FILE__________________")
        print("")
        print("")
except IndexError:
    pass
