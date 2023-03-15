import numpy as np
import torch
import torch.nn as nn
import torch.nn.functional as F
import math, copy, time
import matplotlib.pyplot as plt
import seaborn
seaborn.set_context(context="talk")
from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')