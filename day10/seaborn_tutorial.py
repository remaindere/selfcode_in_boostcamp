import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid") # default style, darkgrid
#print(sns.get_dataset_names()) #see default data set names
# ['anagrams', 'anscombe', 'attention', 'brain_networks', 
# 'car_crashes', 'diamonds', 'dots', 'exercise', 'flights', 
# 'fmri', 'gammas', 'geyser', 'iris', 'mpg', 'penguins', 
# 'planets', 'tips', 'titanic']
boarding_list = sns.load_dataset("titanic") # dataset "titanic"
#print(boarding_list)
# sns.relplot(x="sex",y="survived", kind="line",data=boarding_list)
# plt.show()
#print(boarding_list.keys())
# sns.relplot(x="pclass", y="survived", kind="line", data=boarding_list)
# plt.show()

# sns.relplot(x="age",y="survived", kind="line",col="deck",data=boarding_list)
# plt.show()

sns.violinplot(x="survived",y="age",hue="sex",data=boarding_list)
plt.show()

print(boarding_list.groupby(['deck','pclass'])['age'].mean('survived'))
