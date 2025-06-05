# Курсовая работа: Прогнозирование эффективности химических соединений

## Описание проекта

Данный проект посвящён разработке моделей машинного обучения для прогнозирования эффективности химических соединений против вируса гриппа.

 Реализованы задачи:
- **Регрессия**: прогноз значений IC50, CC50, SI
- **Классификация**: определение, превышают ли значения медиану и порог 8 (для SI)

 Используемые алгоритмы:
- Logistic Regression
- Random Forest
- Gradient Boosting
- CatBoost Regressor
- LightGBM (в т.ч. с автоматическим подбором от FLAML)
- XGBoost
- VotingRegressor (ансамбль моделей)

---

##  Структура проекта

<pre>drug-discovery-ml/
├── regression/
│ ├── regression_ic50.ipynb
│ ├── regression_cc50.ipynb
│ └── regression_si.ipynb
│
├── classification/
│ ├── classification_ic50_median.ipynb
│ ├── classification_cc50_median.ipynb
│ ├── classification_si_median.ipynb
│ └── classification_si_gt8.ipynb
│
├── utils/
│ └── prepare_data.py
│
├── eda_analysis.ipynb
├── kurs.xlsx
├── report.md / report.pdf
├── requirements.txt
└── README.md</pre>
---

## Результаты моделей

### Регрессия
| Цель    | RMSE  | R²    |
|---------|--------|--------|
| log_IC50 | 1.415 | 0.480 |
| log_CC50 | 1.115 | 0.445 |
| log_SI   | 1.174 | 0.350 |

### Классификация
| Цель            | Accuracy | F1     | ROC-AUC |
|------------------|----------|--------|---------|
| IC50 > медианы   | 0.51     | 0.34   | 0.4687  |
| CC50 > медианы   | 0.49     | 0.32   | 0.5236  |
| SI > медианы     | 0.67     | 0.66   | 0.7077  |
| SI > 8           | 0.79     | 0.79   | 0.8710  |

---

## Используемые библиотеки

- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `xgboost`
- `lightgbm`
- `catboost`
- `joblib`
- `openpyxl`

---

##  Как запустить

1. Клонировать репозиторий:

```bash
git clone https://github.com/sstanna/drug-discovery-ml.git
cd drug-discovery-ml
