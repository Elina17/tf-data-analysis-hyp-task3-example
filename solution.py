import pandas as pd
import numpy as np
from scipy.stats import mannwhitneyu

chat_id = 1171143592 # Ваш chat ID, не меняйте название переменной

def solution(...) -> bool: # Одна или две выборке на входе, заполняется исходя из условия
    res = mannwhitneyu(x, y, alternative='less')
    return res.pvalue < 0.09
