from sklearn.ensemble import IsolationForest

# load logs
with open("data/logs.txt", "r") as f:
    logs = f.readlines()


# true labels (1 = suspicious, 0 = normal)
true_labels = [0, 1, 0, 1, 0, 1, 1]


# ---------- Rule-based part ----------
keywords = ["error", "failed", "unauthorized", "invalid"]

rule_flags = []

for line in logs:
    text = line.lower()
    flag = 0

    for word in keywords:
        if word in text:
            flag = 1
            break

    rule_flags.append(flag)


# ---------- ML part ----------
# simple numeric representation (length of log line)

data = [[len(line)] for line in logs]

model = IsolationForest(contamination=0.3)
model.fit(data)

ml_preds = model.predict(data)  # 1 = normal, -1 = anomaly


# ---------- Hybrid ----------
hybrid_flags = []

for i in range(len(logs)):
    if rule_flags[i] == 1 or ml_preds[i] == -1:
        hybrid_flags.append(1)
    else:
        hybrid_flags.append(0)


# ---------- Output ----------
print("\nResults:\n")

for i in range(len(logs)):
    print("Log:", logs[i].strip())
    print("Rule:", rule_flags[i],
          "| ML:", ml_preds[i],
          "| Hybrid:", hybrid_flags[i])
    print("-" * 40)

# -------- Evaluation --------

tp = 0
fp = 0
fn = 0

for i in range(len(true_labels)):
    if hybrid_flags[i] == 1 and true_labels[i] == 1:
        tp += 1
    elif hybrid_flags[i] == 1 and true_labels[i] == 0:
        fp += 1
    elif hybrid_flags[i] == 0 and true_labels[i] == 1:
        fn += 1

precision = tp / (tp + fp) if (tp + fp) != 0 else 0
recall = tp / (tp + fn) if (tp + fn) != 0 else 0
f1 = (2 * precision * recall) / (precision + recall) if (precision + recall) != 0 else 0

print("\n--- Evaluation ---")
print("Precision:", round(precision, 2))
print("Recall:", round(recall, 2))
print("F1-score:", round(f1, 2))