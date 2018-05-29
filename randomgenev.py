import seaborn as sns
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randint(low=0,high=9,size =(1,10000000)))

sns.countplot(data = df)
