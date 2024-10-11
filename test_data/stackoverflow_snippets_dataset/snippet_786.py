# Extracted from https://stackoverflow.com/questions/31594549/how-to-change-the-figure-size-of-a-seaborn-axes-or-figure-level-plot
import seaborn as sns 

g = sns.catplot(data=df, x='xvar', y='yvar', hue='hue_bar')
g.fig.set_figwidth(8.27)
g.fig.set_figheight(11.7)

