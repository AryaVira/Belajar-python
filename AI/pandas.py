import pandas as pd

data = pd.read_csv('C:/Users/hardjono/belajar python/Occupancy_Estimation.csv')
print(data.head())

print("ukuran data set (baris, kolom):", data.shape)

print("/informasi dataset:")
print(data.info())

print("/nNilai unik pada S6_PIR:",data['S6_PIR'].unique())
print("nilai unik pada S7_PIR:", data['S7_PIR'].unique())
print("nilai unik pada Room_Occupancy_Count:", data['Room_Occupancy_Count'].unique())