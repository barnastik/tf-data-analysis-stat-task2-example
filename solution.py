import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1004689536 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:

    from scipy.stats import t
    data = x
    alpha = p
    n = len(data)
    mean = np.mean(data)
    std_err = np.std(data, ddof=1) / np.sqrt(n)
    t_score = t.ppf(1 - alpha / 2, n - 1)
    lower_bound = mean - t_score * std_err
    upper_bound = mean + t_score * std_err
    return (lower_bound, upper_bound)
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
