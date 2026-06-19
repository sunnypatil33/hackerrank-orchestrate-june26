import pandas as pd
import os

INPUT_FILE = "../dataset/test.csv"
OUTPUT_FILE = "../output.csv"


df = pd.read_csv(INPUT_FILE)

results = []

for i, row in df.iterrows():
    claim_id = row.get("claim_id", i)

    conversation = str(row.get("conversation", "")).lower()

    issue_type = "unknown"
    part = "unknown"
    decision = "not_enough_info"
    severity = "low"

    if "crack" in conversation or "broken" in conversation:
        issue_type = "crack"
        decision = "supported"
        severity = "high"

    elif "scratch" in conversation:
        issue_type = "scratch"
        decision = "supported"
        severity = "low"

    if "car" in conversation:
        part = "car_body"
    elif "laptop" in conversation:
        part = "screen"
    elif "package" in conversation:
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
