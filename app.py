from flask import Flask, request, jsonify
import pandas as pd
import pickle

# ---------- Carrega o modelo ----------
with open("rf_model_career.pkl", "rb") as f:
    package = pickle.load(f)

model = package["model"]
feature_names = package["features"]

app = Flask(__name__)

@app.route("/")
def home():
    return "API de probabilidade de mudança de carreira está no ar 🚀"

@app.route("/predict", methods=["POST"])
def predict():
    # tenta ler JSON
    data = request.get_json()

    if data is None:
        return jsonify({
            "error": "JSON não recebido ou Content-Type incorreto. Envie 'Content-Type: application/json'.",
            "expected_fields": feature_names
        }), 400

    # verifica campos que realmente faltam
    missing = [feat for feat in feature_names if feat not in data]

    if missing:
        return jsonify({
            "error": "Campos faltando no JSON",
            "expected_fields": feature_names,
            "missing_fields": missing
        }), 400

    # monta DataFrame NA MESMA ORDEM DAS FEATURES
    X_input = pd.DataFrame([[data[feat] for feat in feature_names]],
                           columns=feature_names)

    # previsão
    prob = float(model.predict_proba(X_input)[0, 1])
    pred = int(model.predict(X_input)[0])

    return jsonify({
        "probabilidade_mudar": prob,
        "classe_prevista": pred
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
