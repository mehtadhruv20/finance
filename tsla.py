import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as dat
import pandas as pd
import fix_yahoo_finance as yf
yf.pdr_override()
from pandas.api.types import is_list_like
import pandas_datareader.data as web
style.use('ggplot')
start=dt.date(2010,1,1)
end=dt.date(2016,1,1)
df = web.get_data_yahoo('MS', start, end)
df.to_csv('tsla')
hello=pd.read_csv('tsla',parse_dates=True,index_col=0)
col=hello['Adj Close']
col1=col.resample('10D').ohlc()
ax1=plt.subplot2grid(shape=(1,10),loc=(0,8))
hello=hello.values
from sklearn.preprocessing import StandardScaler
s=StandardScaler()
hello=s.fit_transform(hello)
hello=pd.DataFrame(hello)
hello.plot()