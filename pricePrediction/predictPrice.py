import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import pickle
from .supportingClasses import KNNClassifier,MVLinearRegression,knnRegression


def standardize_dataframe_from_scaler(df,columns_to_normalize,scaler):

    normalized_df = df.copy()
    columns_to_normalize = columns_to_normalize
    mean_values = scaler['mean']
    std_values = scaler['std']

    df_standardized = df.copy()
    df_standardized[columns_to_normalize] = ((df[columns_to_normalize] - mean_values) / (std_values))

    return df_standardized

def minmax_scale_dataframe_from_scaler(df,columns_to_normalize,scaler):
    normalized_df = df.copy()
    columns_to_normalize = columns_to_normalize

    # Min-Max scale numeric columns
    min_values = scaler['min']
    max_values = scaler['max']

    df_minmax_scaled = df.copy()
    df_minmax_scaled[columns_to_normalize] = (df[columns_to_normalize] - min_values) / (max_values - min_values)

    return df_minmax_scaled

 
def OLS(Y, Y_hat,N):
    return (1/(2*N))*(np.sum((Y_hat-Y)**2))

def R2(Y, Y_hat,):
    return (1-(np.sum((Y-Y_hat)**2))/np.sum(Y-np.mean(Y)))

  
def standardize_dataframe_from_scaler(df,columns_to_normalize,scaler):

    normalized_df = df.copy()
    columns_to_normalize = columns_to_normalize
    mean_values = scaler['mean']
    std_values = scaler['std']

    df_standardized = df.copy()
    df_standardized[columns_to_normalize] = ((df[columns_to_normalize] - mean_values) / (std_values))

    return df_standardized

def minmax_scale_dataframe_from_scaler(df,columns_to_normalize,scaler):
    normalized_df = df.copy()
    columns_to_normalize = columns_to_normalize

    # Min-Max scale numeric columns
    min_values = scaler['min']
    max_values = scaler['max']

    df_minmax_scaled = df.copy()
    df_minmax_scaled[columns_to_normalize] = (df[columns_to_normalize] - min_values) / (max_values - min_values)

    return df_minmax_scaled


class PricePrediction():
  def __init__(self, data):
    self.load_model()
    self.data = data

  def predictPrice(self):

    self.scaleData()
    print('Scaled The Data')
    classifier = self.models['Classifier']
    X_classify = self.data_normalized[['LAT','LON','CLASS','ZIP']].to_numpy()
    y_hat, y_hat_top_k, weights_top_k = classifier.predict(X_classify,50, k=3)

    print('Got the classifications')

    self.data_normalized['PricePerSqFtCategory'] = y_hat
    self.data_normalized['PredClass'] = y_hat_top_k
    self.data_normalized['PredClassWeights'] = weights_top_k

    self.data_normalized = self.data_normalized.drop(columns=['PricePerSqFtCategory','LAT','LON','ZIP'])

    pretrained_regression = self.models['Regression']
    self.data_normalized['PredPrices'] = None

    print('Starting Regrssion')

    for index, row in self.data_normalized.iterrows():
      pred_price = []
      for cls in row['PredClass']:
        row_df = pd.DataFrame(row).transpose()
        feats = row_df.copy()
        feats = feats.drop(columns=['SalePrice','PredClass','PredPrices','PredClassWeights']).to_numpy()
        reg = pretrained_regression[cls]
        if cls == 4:
          pred = reg.predict_single(feats,3)
        else:
          pred = reg.predict(feats)
        pred_price.append(pred)
      self.data_normalized.at[index,'PredPrices'] = pred_price

    predicted_prices = self.data_normalized['PredPrices'].to_numpy()
    predicted_prices_weights = self.data_normalized['PredClassWeights'].to_numpy()

    print('Got Predictions')
    print('Weighting the Predictions')

    final_pred = []
    for i in range (0,len(predicted_prices)):
      values = [float(arr[0]) for arr in predicted_prices[i]]
      weights = predicted_prices_weights[i]
      weights = [0 if value is None else value for value in weights]
      # weights = [(min(weights)) if value == 0 else value for value in weights]
      weighted_average = sum(value * weight for value, weight in zip(values, weights)) / sum(weights)
      final_pred.append(weighted_average)

    print('Done .!')


    return final_pred, predicted_prices, weights

  def scaleData(self):
    scaler = self.models['Scaler']
    self.data_normalized = self.data.copy()
    columns_to_normalize = ['IntendedUse', 'Deed', 'Financing', 'BuyerSellerRelated',
                            'Solar', 'PersonalProperty', 'PartialInterest', 'STORIES',
                            'SQFT', 'LON', 'LAT','ZIP','CLASS']
    self.data_normalized = minmax_scale_dataframe_from_scaler(df=self.data,columns_to_normalize=columns_to_normalize,scaler=scaler)


  def load_model(self):
    file_path = 'pricePrediction/trained_model_Pima11.pkl'
    with open(file_path, 'rb') as pickle_file:
      loaded_models = pickle.load(pickle_file)
    self.models = loaded_models
    
