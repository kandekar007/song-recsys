import os
import numpy as np
import pandas as pd
import pickle

import seaborn as sns
#import plotly.express as px 
import matplotlib.pyplot as plt
# %matplotlib inline

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.metrics import euclidean_distances
from scipy.spatial.distance import cdist

import warnings
warnings.filterwarnings("ignore")

## created data1.csv to pass in recommender function and scalar is passed using pickle ##

# data=pd.read_csv("D:\Placements\WebDev\SongRecommender_v1.0\SongRecommender\\app\data_o.csv")
# root="\\."
# os.chdir(root)
path =  os.path.abspath("./app/data_o.csv")
data=pd.read_csv(path)
data['liveness_log']=np.log1p(data['liveness'])
#data['popularity_log']=np.log1p(data['popularity'])
data['speechiness_log']=np.log1p(data['speechiness'])
data['duration_ms_log']=np.log1p(data['duration_ms'])
data['loudness_log']=-np.log1p(-data['loudness'])

data1=data.copy()
dropcolumn= ['duration_ms_log','instrumentalness','loudness_log','speechiness_log', 'liveness_log', 'loudness']
data1.drop(dropcolumn, axis=1, inplace=True)

data1.dropna(how='any',inplace=True)
# data1.to_csv('data_preprocessed.csv')





