# open and create a file
# object f and add file contents
# to list object 'story'
with open('story.txt') as f:
    story = f.readlines()


# print the first line of story
# for i, j in enumerate(story):
#     if i == 0:
#         print(j)
# print(story[0])

# # print the last line of story
# # for i, j in enumerate(story):
# #     if i == len(story)-1:
# #         print(j)
# print(story[len(story)-1])


# # print the even lines of story
# for i, j in enumerate(story):
#     if i % 2 != 0:
#         print(j)

# # print the odd lines of story
# for i, j in enumerate(story):
#     if i % 2 == 0:
#         print(j)


# open and create a file
# object f and add file contents
# to list object 'name_list'
with open('names.txt') as f:
    name_list = f.readlines()

for i in name_list:
    print(i, end='')

print()


# if the name starts with 'i', print that name
for i in name_list:
    if i.startswith('I'):
        print(i)


# sort the names in ascending order
# and write them to names_sorted.txt
def sort_names():
    names_sorted = sorted(name_list)
    with open('names_sorted.txt', 'w') as f:
        for i in names_sorted:
            f.write(i)


# function call
sort_names()


# add a name that has not previously
# been added to list
def add_name(name):
    # if it exists, do nothing
    if '{}\n'.format(name) not in name_list:
        name_list.append('{}\n'.format(name))
    # write all the names to name.txt
    with open('names.txt', 'w') as f:
        for i in name_list:
            f.write(i)


# function call
add_name('Christopher')
add_name('Michael')
add_name('Jonathan')

sort_names()
