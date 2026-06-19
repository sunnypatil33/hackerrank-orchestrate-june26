import pandas as pd
import os

INPUT_FILE = "../dataset/claims.csv"
OUTPUT_FILE = "../output.csv"

df = pd.read_csv(INPUT_FILE)

results = []

for i, row in df.iterrows():
    claim_id = row.get("claim_id", i)

    conversation = str(row.get("claim_description", "")).lower()
    obj = str(row.get("object_type", "")).lower()

    # 🔥 DEFAULT CHANGE
    if conversation.strip() != "":
        decision = "supported"
        issue_type = "damage"
        severity = "medium"
    else:
        decision = "not_enough_info"
        issue_type = "unknown"
        severity = "low"

    # object mapping
    if "car" in obj:
        part = "car_body"
    elif "laptop" in obj:
        part = "screen"
    elif "package" in obj:
        part = "box"
    else:
        part = "unknown"

    results.append({
        "claim_id": claim_id,
        "decision": decision,
        "issue_type": issue_type,
        "part": part,
        "severity": severity
    })

out = pd.DataFrame(results)
out.to_csv(OUTPUT_FILE, index=False)

print("Done! output.csv")
