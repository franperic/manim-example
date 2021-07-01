import numpy as np
import pandas as pd

np.random.seed(54)

df = pd.DataFrame(
    {
        "date": pd.date_range(start="2021-01-01", end="2021-07-01", freq="D"),
        "var1": np.random.randint(low=100, high=500, size=182),
        "var2": np.random.randint(low=100, high=500, size=182),
    }
)

df.to_csv("data/illustration.csv", index=False)
