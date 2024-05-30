import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import process
from sqlalchemy import create_engine

# Heatmap oluşturmak için bir fonksiyon tanımlayalım.
def create_heatmap():
    
    process.process_data('weather_2016_2020_daily.csv') #elimizde 'weather_with_hdd_cdd.csv' var

    # Veriyi PostgreSQL'den çek
    #df = pd.read_sql_query("SELECT * FROM weather_with_hdd_cdd", conn)

    df = pd.read_csv('weather_with_hdd_cdd.csv', delimiter = ",", skiprows = 0, low_memory = False)

    # Drop the unnecessary columns
    df = df.drop('Date', axis=1)
    
    
    correlation_matrix = df.corr()

    # Korelasyon matrisini DataFrame'e dönüştür
    correlation_df = pd.DataFrame(correlation_matrix)

    ###############################################################################################

    engine = create_engine('postgresql://postgres:123456@localhost:5432/postgres')

     # DataFrame'i PostgreSQL veritabanına tablo olarak ekle
    correlation_df.to_sql('correlation_table', engine, if_exists='replace')

    # Heatmap'i oluştur
    plt.figure(figsize=(16, 10))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Correlation Heatmap')
    plt.show()

    