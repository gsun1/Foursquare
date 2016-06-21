import pandas as pd
import statsmodels.api as sm
import pylab as pl
import numpy as np


df = pd.read_csv('regress.csv')



logit = sm.Logit(df['Recommended'], df['Times'])

result = logit.fit()

print(result.summary())

#pl.plot(df['Recommended'],df['Times'], 'bo')
#pl.show()