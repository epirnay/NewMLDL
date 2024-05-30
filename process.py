import pandas as pd
from sklearn.preprocessing import LabelEncoder

def process_data(file_name):

    df = pd.read_csv(file_name, delimiter = ",", skiprows = 0, low_memory = False)

    df['Temp_avg_C'] = (df['Temp_avg'] - 32) * 5.0/9.0

    df['HDD'] = df['Temp_avg_C'].apply(lambda x: max(0, 18.3 - x))
    df['CDD'] = df['Temp_avg_C'].apply(lambda x: max(0, x - 18.3))

    
    m = df.shape[0]
    p2 = pd.Series(range(m), pd.period_range('2016-06-01', freq = '1D', periods = m))
    df['Date'] = p2.to_frame().index

    ## LabelEncoder sınıfını oluştur
    label_encoder = LabelEncoder()
    # Tarih değerlerini numeric değerlere dönüştür
    df['Date_encoded'] = label_encoder.fit_transform(df['Date'])


    null_percentage = df.isnull().sum() * 100 / df.shape[0]
    print("Null percentage:")
    print(null_percentage)

    df = df.dropna() #drop if there is a null value
    
    df.to_csv('weather_with_hdd_cdd.csv', index=False)
    
    #df.to_sql('weather_with_hdd_cdd', conn, index=False, if_exists='replace')

  
