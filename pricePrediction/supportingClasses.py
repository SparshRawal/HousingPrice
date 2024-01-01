import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import pickle

class KNNClassifier():

  def fit(self, X, y):
    self.X=X
    self.y=y

  def predict(self, X, K, epsilon =1e-6, k=2 ):

    N=len(X)
    y_hat = np.zeros(N)
    y_hat_top_k = []
    weights_top_k = []
    for i in range(N):
      dist2 = np.sum((self.X-X[i])**2, axis=1)
      idxt  = np.argsort(dist2)[: K]
      gamma_k = np.nan_to_num(1/(np.sqrt(dist2[idxt]+epsilon)))

      top_k_predictions  = np.argsort(np.bincount(self.y[idxt], weights= gamma_k))[::-1]


      y_hat[i] = np.bincount(self.y[idxt], weights= gamma_k).argmax()
      y_hat_top_k.append(top_k_predictions[:k])

      # Calculating weights

      unique_values, counts = np.unique(self.y[idxt], return_counts=True)
      percentage = (counts / len(self.y[idxt]))
      result_dict = dict(zip(unique_values, percentage))
      weights = []
      for value in y_hat_top_k[0]:
        weights.append(result_dict.get(value))
      weights_top_k.append(weights)


    return y_hat , y_hat_top_k, weights_top_k
    
class MVLinearRegression():
  def fit(self, X, y, eta = 1e-3, epochs=1e3, show_curve = False):
    epochs = int(epochs)
    N, D  =  X.shape
    Y  = y

    #Begin Optimization
    self.W = np.random.randn(D)
    J  = np.zeros(epochs)

    #SGD
    for epoch in range(epochs):
      Y_hat = self.predict(X)
      J[epoch] = OLS(Y,Y_hat,N)

      #Weight update
      self.W -= eta * ((1/N)*(X.T@(Y_hat-Y)))

    if show_curve:
      plt.figure()
      plt.plot(J)
      plt.xlabel("Epochs")
      plt.ylabel("$\mathcal{J}$")
      plt.title("Training curve")
      plt.show()

  def predict(self, X):
    return X@self.W

class knnRegression():
  def fit(self,X, y):
    self.X=X
    self.y=y
  def predict(self, X, K, epsilon =1e-9):
    N=len(X)
    y_hat = np.zeros(N)
    for i in range(N):
      dist2 = np.sum((self.X-X[i])**2, axis=1)
      idxt  = np.argsort(dist2)[: K]
      gamma_k = (np.exp(-dist2[idxt]))/(np.exp(-dist2[idxt]).sum())
      y_hat[i] = np.dot(self.y[idxt].T,gamma_k)
    return y_hat
  def predict_single(self, X, K, epsilon =1e-9):
    N=len(X)
    y_hat = np.zeros(N)
    for i in range(N):
      dist2 = np.sum((self.X-X[i])**2, axis=1)
      idxt  = np.argsort(dist2)[: K]

      gamma_k = (np.exp([-dist2[id] for id in idxt]))/(np.exp([-dist2[id] for id in idxt]).sum()) # Was Giving error for a single Data Point

      y_hat[i] = np.dot(self.y[idxt].T,gamma_k)
    return y_hat
  
def OLS(Y, Y_hat,N):
    return (1/(2*N))*(np.sum((Y_hat-Y)**2))

def R2(Y, Y_hat,):
    return (1-(np.sum((Y-Y_hat)**2))/np.sum(Y-np.mean(Y)))