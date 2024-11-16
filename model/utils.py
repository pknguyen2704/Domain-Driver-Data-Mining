import numpy as np
import pandas as pd
import re
from sklearn.model_selection import train_test_split

def clean_content(text):
    text = re.sub(r'\s+', ' ', text)
    text = re.sub(r'[^\w\s]', '', text)
    return text.strip().lower()