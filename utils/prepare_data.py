import pandas as pd
import numpy as np
from sklearn.impute import SimpleImputer

def load_and_prepare_data(path="../kurs.xlsx"):
    # ⬆ путь исправлен на "../kurs.xlsx", чтобы искать файл выше на один уровень
    df = pd.read_excel(path, engine='openpyxl')
    df.drop(columns=['Unnamed: 0'], inplace=True, errors='ignore')
    df.dropna(axis=1, how='all', inplace=True)

    # Логарифмирование целевых признаков
    df['log_IC50'] = np.log1p(df['IC50, mM'])
    df['log_CC50'] = np.log1p(df['CC50, mM'])
    df['log_SI'] = np.log1p(df['SI'])

    # Бинаризация целевых признаков
    df['cls_ic50_median'] = (df['IC50, mM'] > df['IC50, mM'].median()).astype(int)
    df['cls_cc50_median'] = (df['CC50, mM'] > df['CC50, mM'].median()).astype(int)
    df['cls_si_median'] = (df['SI'] > df['SI'].median()).astype(int)
    df['cls_si_gt8'] = (df['SI'] > 8).astype(int)

    # Фичи
    targets = ['IC50, mM', 'CC50, mM', 'SI', 'log_IC50', 'log_CC50', 'log_SI',
               'cls_ic50_median', 'cls_cc50_median', 'cls_si_median', 'cls_si_gt8']
    X_raw = df.drop(columns=targets)

    imputer = SimpleImputer(strategy='mean')
    X = pd.DataFrame(imputer.fit_transform(X_raw), columns=X_raw.columns)

    return {
        'X': X,
        'y_ic50': df['log_IC50'],
        'y_cc50': df['log_CC50'],
        'y_si': df['log_SI'],
        'cls_ic50_median': df['cls_ic50_median'],
        'cls_cc50_median': df['cls_cc50_median'],
        'cls_si_median': df['cls_si_median'],
        'cls_si_gt8': df['cls_si_gt8']
    }
