# def letter_counter(filename,to_count):
#     newFile=open(filename,'r')
#     inpFile=newFile.read()
#     word={}
#     for i in inpFile:
#         i=i.lower()
#         if i in to_count and i not in word:
#             word[i]=1
#         elif i in to_count and i in word:
#             word[i]=word[i]+1
#     return word
# print(letter_counter("sample.txt",'aeiou'))
def remove_item(list_item,to_remove):
    new=[]
    for i in list_item:
        if to_remove not in list_item:
            return "This item is not in list"
        elif i != to_remove:
            new.append(i)
    return new
print(remove_item([1,2,34,7,5],7)) #remove item program
