import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder
from sklearn.decomposition import PCA

data = pd.read_csv('3.4.iris_dataset.csv')

#print(data.columns)

X = data[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)','petal width (cm)']]

kmeans = KMeans(n_clusters=3,random_state=42)
data['Clusters'] = kmeans.fit_predict(X)

le = LabelEncoder()
true_labels = le.fit_transform(data['target'])

pca = PCA(n_components=2)
pca_features = pca.fit_transform(X)

plt.figure(figsize=(8,5))
plt.scatter(pca_features[:,0],pca_features[:,1],c=data['Clusters'])
plt.title('KMeans Clustering on Iris Dataset (PCA Projection)')
plt.xlabel('PCA Component 1')
plt.ylabel('PCA Component 2')
plt.grid()
plt.show()