import pickle

liste = ["Hello", 8, "World", 9]

file = open("new.pickle", "wb")
pickle.dump(liste, file)
file.close()

file2 = open("new.pickle", "rb")
al = pickle.load(file2)
print(al)
file2.close()

