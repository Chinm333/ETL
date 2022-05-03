# part1
# with open("chinm.txt") as file:
#     # I have opened the chinm.txt file
#     content = file.read()
#     # I have read the file
#     # print(content.upper())
#     x = content.upper()
#     # The file is now transformed into upper case
#     with open("output/output.txt", "w") as oupt:
#         # I want to the directory called output and create output.text file and wrote the content in the output.txt
#         # file.
#         oupt.write(x)

# part2
with open("chinm1.txt") as file:
    # I have opened the chinm.txt file
    search = input("Enter the word that is needed to be counted!\n").lower()
    content = file.read().lower()
    x = content.split()
    # print(x.count(search))
    counting = x.count(search)
    with open("output/output2.txt", "w") as oup:
        oup.write(str(f"{search}:{counting}"))
