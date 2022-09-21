

path = "data/lincoln_joyce/ribozyme.txt"


with open(path, 'r') as file:
    data = file.read()


# 
# a_count = data.count('a')
# g_count = data.count('g')
# c_count = data.count('c')
# u_count = data.count('u')
# 

def clean_ribozyme(raw):
    drop_chars = ['5','P','O','H','3','\'','-','\n']
    for x in drop_chars:
        data = data.replace(x, '')


print(type(data))
print(data)
