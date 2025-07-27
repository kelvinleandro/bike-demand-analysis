import numpy as np
from sklearn.metrics import mean_squared_log_error, r2_score, mean_absolute_error


def evaluate_model(y_true, y_pred, model_name="Modelo"):
    """
    Calcula e imprime as principais métricas de regressão.
    RMSLE, R² e MAE.
    """
    y_pred = np.maximum(y_pred, 0)

    rmsle = np.sqrt(mean_squared_log_error(y_true, y_pred))
    r2 = r2_score(y_true, y_pred)
    mae = mean_absolute_error(y_true, y_pred)

    print(f"--- Desempenho do {model_name} ---")
    print(f"RMSLE (Root Mean Squared Log Error): {rmsle:.4f}")
    print(f"R² (Coeficiente de Determinação):    {r2:.4f}")
    print(f"MAE (Mean Absolute Error):           {mae:.2f} aluguéis")
    print("----------------------------------------")

    return {"rmsle": rmsle, "r2": r2, "mae": mae}
