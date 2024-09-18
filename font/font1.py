import matplotlib
from matplotlib import font_manager

#All fonts
fonts = set([f.name for f in matplotlib.font_manager.fontManager.ttflist])
print(fonts)

