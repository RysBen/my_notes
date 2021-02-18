import pandas as pd
from statsmodels.formula.api import ols 
from statsmodels.stats.anova import anova_lm
import scipy.stats as ss

############
# one way
############

# prepare
df = pd.read_csv('oneway.csv')
a = df[df['algo'] == 'a']['ratio']
b = df[df['algo'] == 'b']['ratio']

# 1/4: 正态性
ss.normaltest(a); ss.normaltest(b)

# 2/4: 方差齐性
args=[a,b]
ss.levene(*args)

# F test
ss.f_oneway(*args)

# F test too
model = ols('ratio ~ algo', df).fit()
anovat = anova_lm(model)
