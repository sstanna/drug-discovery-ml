# Курсовая работа: Прогнозирование эффективности химических соединений

## Описание проекта

Данный проект посвящён разработке моделей машинного обучения для прогнозирования эффективности химических соединений против вируса гриппа.

 Реализованы задачи:
- **Регрессия**: прогноз значений IC50, CC50, SI
- **Классификация**: определение, превышают ли значения медиану и порог 8 (для SI)

 Используемые алгоритмы:
- `RandomForest`
- `GradientBoosting`

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

| Цель      | RMSE    | R²     |
|-----------|---------|--------|
| log_IC50  | ~0.798  | ~0.71  |
| log_CC50  | ~0.881  | ~0.68  |
| log_SI    | ~0.762  | ~0.73  |


### Классификация

| Цель             | Accuracy | F1     | ROC-AUC |
|------------------|----------|--------|---------|
| IC50 > медианы   | ~0.81    | ~0.80  | ~0.88   |
| CC50 > медианы   | ~0.78    | ~0.76  | ~0.85   |
| SI > медианы     | ~0.72    | ~0.71  | ~0.80   |
| SI > 8           | ~0.85    | ~0.84  | ~0.91   |

---

## Используемые библиотеки

- `pandas`
- `numpy`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `openpyxl`

---

##  Как запустить

1. Клонировать репозиторий:

```bash
git clone https://github.com/sstanna/drug-discovery-ml.git
cd drug-discovery-ml
