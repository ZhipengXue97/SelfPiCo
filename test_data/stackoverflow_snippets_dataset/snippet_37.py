# Extracted from https://stackoverflow.com/questions/332289/how-do-i-change-the-size-of-figures-drawn-with-matplotlib
x_inches = 150*(1/25.4)     # [mm]*constant
y_inches = x_inches*(0.8)
dpi = 96

fig = plt.figure(1, figsize = (x_inches,y_inches), dpi = dpi, constrained_layout = True)

