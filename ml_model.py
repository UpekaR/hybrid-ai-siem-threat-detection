from sklearn.ensemble import IsolationForest

# sample numeric data (fake it for now)
# later will use real log features

data = [
    [1],
    [2],
    [1],
    [2],
    [100],   # anomaly
    [2],
    [1]
]

model = IsolationForest(contamination=0.2)
model.fit(data)

predictions = model.predict(data)

print("Predictions:", predictions)