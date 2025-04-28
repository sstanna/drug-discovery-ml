# Курсовая работа: Прогнозирование эффективности химических соединений

## 📚 Описание проекта

В этом проекте разработаны модели машинного обучения для прогнозирования эффективности химических соединений против вируса гриппа.

Построены модели:
- Регрессии (IC50, CC50, SI)
- Классификации (IC50 > медианы, CC50 > медианы, SI > медианы, SI > 8)

Методы:
- Случайный лес (RandomForest)
- Градиентный бустинг (GradientBoosting)

---

## 📂 Структура проекта
drug-discovery-ml/
├── regression/
│   ├── regression_ic50.ipynb
│   ├── regression_cc50.ipynb
│   └── regression_si.ipynb
│
├── classification/
│   ├── classification_ic50_median.ipynb
│   ├── classification_cc50_median.ipynb
│   ├── classification_si_median.ipynb
│   └── classification_si_gt8.ipynb
│
├── utils/
│   └── prepare_data.py
│
├── report.md
├── requirements.txt
├── README.md  


---

## 🛠 Используемые библиотеки

- pandas
- numpy
- scikit-learn
- matplotlib
- seaborn
- openpyxl

---

## 📈 Метрики моделей

- RMSE, R² для регрессии
- Accuracy, F1, ROC-AUC для классификации

---

## 🚀 Как запустить

1. Установить зависимости:
```bash
pip install -r requirements.txt
