



# Orienting module first looking around the metadata of https://www.kaggle.com/datasets/samuelcortinhas/rsna-2022-spine-fracture-detection-metadata/data,
# this is NOT my data. So credit to Kaggle & Samuel Cortinhas
import pandas as pd


# Get the data files of meta train meta segment train segment to peak around with
meta_train = pd.read_csv('data/meta_train_clean.csv')
meta_segmentation = pd.read_csv('data/meta_segmentation_clean.csv')
train_segmented = pd.read_csv('data/train_segmented.csv')

# print the info
print(meta_train.head())
print(meta_segmentation.head())
print(train_segmented.head())
