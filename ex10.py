print ("I am 6'2\" tall.")
print ('I am 6\'2" tall.')

tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\n on a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishes
\t* Catnip\n\t* Grass
"""
print (tabby_cat)
print (persian_cat)
print (backslash_cat)
print (fat_cat)

count = 0
while True:
    for i in ["/","-","|","\\","|"]:
        print ("%s\r" % i,)
    count += 1
    print(count)
    if count == 10:
        break 