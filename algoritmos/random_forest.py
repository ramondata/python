import pandas as pd
from matplotlib import pyplot as plt
from sklearn.tree import plot_tree
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
X, y = make_classification(n_samples=1000, n_features=4, n_informative=2, n_redundant=0, random_state=0, shuffle=False)
clf = RandomForestClassifier(n_estimators = 5, max_depth=2, random_state=0)
clf.fit(X, y)
print(clf.predict([[0,0,0,0]]))

print(clf.feature_importances_)

pd.concat([pd.DataFrame(X,columns=['atr1','atr2','atr3','atr4']),pd.DataFrame(y, columns=['class'])] , axis=1)

for tf in clf.estimators_:
    print("-----------------------------")
    plot_tree(tf, filled=True)
    plt.show()