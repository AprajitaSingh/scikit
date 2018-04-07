#program to load and display datasets
from sklearn import datasets
iris=datasets.load_iris()
digits=datasets.load_digits()
print(digits.data)
print(iris.data)
digits.target
digits.images[0]