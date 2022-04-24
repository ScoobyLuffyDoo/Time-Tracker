import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_theme(style="darkgrid")
fmri = sns.load_dataset("fmri")
data = []

sns.relplot(x="timepoint", y="signal", hue="region", style="event",
            kind="line", data=fmri);
plt.show()