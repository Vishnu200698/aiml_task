#!/usr/bin/env python
# coding: utf-8

# In[21]:


import streamlit as st

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# In[22]:


data=load_iris()
df=pd.DataFrame(data.data,columns=data.feature_names)
df['target']=data.target
df


# In[23]:


X=df.drop(columns=['target'])
y=df['target']


# In[24]:


# split the data into train and test sets

X_train, X_test, y_train, y_test=train_test_split(X,y,test_size=0.2,random_state=42)

#Train Decision Tree Classifier 
clf=DecisionTreeClassifier()
clf.fit(X_train,y_train)


# In[25]:


# Compute accuracy

predictions=clf.predict(X_test)
accuracy=accuracy_score(y_test, predictions)


# In[26]:


# Streamlit UI
st.title("Decision Tree Classifier - Iris Dataset")
st.write(f"Model Accuracy: {accuracy:.2f}")

st.sidebar.header("Input Features")
sepal_length = st.sidebar.slider("Sepal Length", float(df.iloc[:, 0].min()), float(df.iloc[:, 0].max()), float(df.iloc[:, 0].mean()))
sepal_width = st.sidebar.slider("Sepal Width", float(df.iloc[:, 1].min()), float(df.iloc[:, 1].max()), float(df.iloc[:, 1].mean()))
petal_length = st.sidebar.slider("Petal Length", float(df.iloc[:, 2].min()), float(df.iloc[:, 2].max()), float(df.iloc[:, 2].mean()))
petal_width = st.sidebar.slider("Petal Width", float(df.iloc[:, 3].min()), float(df.iloc[:, 3].max()), float(df.iloc[:, 3].mean()))


# In[28]:


# prediction

data_input=np.array([[sepal_length, sepal_width, petal_length, petal_width]])
prediction=clf.predict(data_input)
predicted_class=data.target_names[prediction[0]]

st.subheader("Prediction")
st.write(f'Predicted Class: **{predicted_class}**')


# In[ ]:


# Print the decion tree
if st.button("Show Decision Tree Diagram"):
    fig, ax = plt.subplots(figsize=(12, 8))
    tree.plot_tree(clf, feature_names=data.feature_names, class_names=data.target_name,filled=True, ax=ax)
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek (0)
    st.image(buf, caption="Decision Tree Visualization", use_column_width=True)


# In[ ]:




