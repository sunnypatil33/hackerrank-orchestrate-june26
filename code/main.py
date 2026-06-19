import pandas as pd
import os

INPUT_FILE = "../dataset/claims.csv"
OUTPUT_FILE = "../output.csv"

df = pd.read_csv(INPUT_FILE)

results = []

for i, row in df.iterrows():
    claim_id = row.get("claim_id", i)

    conversation = str(row.get("claim_description", "")).lower()

    issue_type = "unknown"
    part = "unknown"
    decision = "not_enough_info"
    severity = "low"


    if any(word in conversation for word in ["crack", "broken", "damage", "shattered"]):
        issue_type = "damage"
        decision = "supported"
        severity = "high"

    elif any(word in conversation for word in ["scratch", "scratched", "minor"]):
        issue_type = "scratch"
        decision = "supported"
        severity = "low"

    elif any(word in conversation for word in ["dent", "hit", "fell", "issue", "problem"]):
        issue_type = "damage"
        decision = "supported"
        severity = "medium"

    
    obj = str(row.get("object_type", "")).lower()

    if "car" in obj:
        part = "car_body"
    elif "laptop" in obj:
        part = "screen"
    elif "package" in obj:
        part = "box"

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
