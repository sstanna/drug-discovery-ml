import papermill as pm

# Список всех ноутбуков проекта
notebooks = [
    "eda_analysis.ipynb",
    "regression/regression_ic50.ipynb",
    "regression/regression_cc50.ipynb",
    "regression/regression_si.ipynb",
    "classification/classification_ic50_median.ipynb",
    "classification/classification_cc50_median.ipynb",
    "classification/classification_si_median.ipynb",
    "classification/classification_si_gt8.ipynb"
]

# Выполнение каждого ноутбука
for notebook in notebooks:
    print(f"▶️ Выполняем ноутбук: {notebook}")
    pm.execute_notebook(
        notebook,
        notebook,  # сохраняем результат в тот же файл
        parameters={}
    )

print("✅ Все ноутбуки успешно выполнены и сохранены.")
