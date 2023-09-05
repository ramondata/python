import numpy as np
import pandas as pd
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
dataset = pd.read_csv(url, names=names)

from sklearn.model_selection import train_test_split
X = dataset.drop('Class', 1)
y = dataset['Class']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

from sklearn.decomposition import PCA

from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score

for i in range(X_train.shape[1]):
    pca = PCA(n_components=i+1)
    pca_X_train = pca.fit_transform(X_train)
    pca_X_test = pca.transform(X_test)

    classifier = RandomForestClassifier(max_depth=2, random_state=0)
    classifier.fit(pca_X_train, y_train)

    # Predicting the Test set results
    y_pred = classifier.predict(pca_X_test)
    cm = confusion_matrix(y_test, y_pred)
    print ("---------------------------------------------------------------")
    print("PCA: ", i+1)
    print(cm)
    print('Accuracy:', accuracy_score(y_test, y_pred))
    print('Dataset Var: ', pca_X_train.var())
    
for c in range(pca_X_train.shape[1]):
    print("Component(",c+1,"):", pca_X_train[c].var())
    print("---------------------------------------------------------------")