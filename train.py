from sklearn.linear_model import LinearRegression

# Exemple de données d'entraînement
X_train = [[1], [2], [3], [4], [5]]  # Caractéristiques d'entrée
y_train = [2, 4, 6, 8, 10]  # Valeurs cibles correspondantes

# Création et entraînement du modèle
model = LinearRegression()
model.fit(X_train, y_train)

# Exemple de données de test
X_test = [[6], [7], [8]]  # Caractéristiques d'entrée pour lesquelles nous voulons faire des prédictions

# Prédiction des valeurs correspondantes
y_pred = model.predict(X_test)

# Affichage des prédictions
for i in range(len(X_test)):
    print(f"Caractéristiques : {X_test[i]}, Prédiction : {y_pred[i]}")
