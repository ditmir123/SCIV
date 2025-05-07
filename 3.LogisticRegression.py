import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = pd.read_csv('3.4.iris_dataset.csv')
#print(data.columns)

X = data[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)','petal width (cm)']]
y = data['target']

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.2,random_state=42)

model = LogisticRegression(max_iter=200)
model.fit(X_train,y_train)

y_pred = model.predict(X_test)

print('Accuracy:',accuracy_score(y_test,y_pred))
print('Confusion Matrix:',confusion_matrix(y_test,y_pred))
print('Classification Report:',classification_report(y_test,y_pred))