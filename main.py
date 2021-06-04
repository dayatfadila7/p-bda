import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')


df = pd.read_csv('istanbul_stock_exchange.csv')
# print(df)
df.head(5)

df.shape

#print(df.shape)

plt.figure(figsize=(16,8))
plt.title("HARGA STOCK NIKKEI")
plt.plot(df['NIKKEI'])
plt.xlabel('date', fontsize=16)
plt.ylabel('NIKKEI USD', fontsize=18)
plt.show()
