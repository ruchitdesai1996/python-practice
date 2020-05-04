import pandas as pd
import numpy as np



assetsCode = ['BTC', 'ETH', 'XRP', 'LTC']

crypto_df['open'] = crypto_df[['open', 'asset']].apply(lambda x: float(x[0] * 0.80) if x[1] in assetsCode else np.nan, axis=1)
crypto_df['close'] = crypto_df[['close', 'asset']].apply(lambda x:float(x[0] * 0.80) if x[1] in assetsCode else np.nan, axis=1)
crypto_df['high'] = crypto_df[['high', 'asset']].apply(lambda x:float(x[0] * 0.80) if x[1] in assetsCode else np.nan, axis=1)
crypto_df['low'] = crypto_df[['low', 'asset']].apply(lambda x:float(x[0] * 0.80) if x[1] in assetsCode else np.nan, axis=1)

crypto_df.dropna(inplace=True)

crypto_df.reset_index(drop=True ,inplace=True)

crypto_df = pd. read_csv('crypto-markets.csv')

crypto_df.head()