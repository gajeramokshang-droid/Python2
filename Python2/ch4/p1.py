import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
from sklearn.preprocessing import StandardScaler
df = pd.read_csv('Hotel Reservations.csv')

df.drop('Booking_ID', axis=1, inplace=True)
df.columns = df.columns.str.strip()


df = pd.get_dummies(data=df, drop_first=True)

y = df['booking_status_Not_Canceled']
x = df.drop('booking_status_Not_Canceled', axis=1)


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.transform(x_test)

accuracies = []
k_range = range(1, 21)

for k in k_range:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train_scaled, y_train)
    y_pred_k = knn.predict(x_test_scaled)
    accuracies.append(accuracy_score(y_test, y_pred_k))

best_k = list(k_range)[np.argmax(accuracies)]
print(f"Optimal K Value: {best_k}")
print(f"Highest Accuracy: {max(accuracies):.4f}")

final_model = KNeighborsClassifier(n_neighbors=best_k)
final_model.fit(x_train_scaled, y_train)
y_pred = final_model.predict(x_test_scaled)

print("\n--- Final Model Results ---")
print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


plt.plot(k_range, accuracies, marker='o')
plt.title('K-Value vs. Accuracy')
plt.xlabel('K')
plt.ylabel('Accuracy')
plt.show()
