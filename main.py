# reading logs from the file

with open("data/logs.txt", "r") as f:
    logs = f.readlines()

print("Number of logs:", len(logs))


# checking each log

keywords = ["error", "failed", "unauthorized", "invalid"]

suspicious = []

for line in logs:
    text = line.lower()

    for word in keywords:
        if word in text:
            suspicious.append(line)
            break   # stop checking more words for this line


print("\nSuspicious logs found:", len(suspicious))


# show a few suspicious logs

for i in range(min(5, len(suspicious))):
    print(suspicious[i].strip())