#
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.Series(np.random.rand(1000), index=np.arange(1000))

data.cumsum()

data.plot()

plt.show()
# bar hist box kde area scatter hexbin
# row快 col慢 view快 copy慢 out参数

