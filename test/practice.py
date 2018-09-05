import sys
import pickle

colors = ['red', 'green', 'black']

f = open('file_colors','wb')

pickle.dump(colors, f)

f.close()

del colors

f = open('file_colors', 'rb')

colors = pickle.load(f)

f.close()

print(colors)
