import numpy as np
from sklearn.naive_bayes import BernoulliNB

data = np.loadtxt(open("hw4-data.csv"), delimiter=",", skiprows=1)
X, Y = data[:,:-1], data[:,-1]

clf = BernoulliNB()
clf.fit(X, Y)
test_data = [[1, 0, 0, 0, 0],
             [1, 0, 1, 0, 1],
             [0, 1, 0, 1, 0]]
print(clf.predict_proba(test_data))

'''
RESULTS FOR NBC:

[[0.46720151 0.53279849] 1
 [0.73911226 0.26088774] 0
 [0.36620794 0.63379206]] 1

'''
