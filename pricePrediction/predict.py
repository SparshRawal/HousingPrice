import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
import pickle
from .predictPrice import PricePrediction


def IntendedUse(value):
  ls = ['Unknown','PrimaryRes','NonPrimary','Rental']
  return ls.index(value)

def Deed(value):
  ls = ['Warranty Deed','Joint Tenancy Deed','Other','Quit Claim Deed', 'Contract or Agreement']
  return ls.index(value)

def Financing(value):
  ls = ['Cash','Other']
  return ls.index(value)


def YesNo(value):
  ls = ['No','Yes']
  return ls.index(value) 

class predictPrice():
    def __init__(self, data):
        self.data = data
    def preProcessAndPredict(self):
        df = pd.DataFrame(self.data)
        columns_to_convert = ['CLASS', 'ROOMS', 'QUALITY', 'HEAT', 'COOL', 'BATHFIXTUR','SQFT','GARAGE']
        df[columns_to_convert] = df[columns_to_convert].astype(int)
        columns_to_convert = ['STORIES', 'LON', 'LAT', 'ZIP']
        df[columns_to_convert] = df[columns_to_convert].astype(float)
        df['IntendedUse'] = df['IntendedUse'].apply(IntendedUse)
        df['Deed'] = df['Deed'].apply(Deed)
        df['Financing'] = df['Financing'].apply(Financing)
        df['BuyerSellerRelated'] = df['BuyerSellerRelated'].apply(YesNo)
        df['Solar'] = df['Solar'].apply(YesNo)
        df['PersonalProperty'] = df['PersonalProperty'].apply(YesNo)
        df['PartialInterest'] = df['PartialInterest'].apply(YesNo)
        df['SalePrice']=0
        pricePredictor = PricePrediction(df)
        final_pred, top3preds, weights = pricePredictor.predictPrice()   
        return  final_pred, top3preds, weights
    
      
