import pandas as pd

INPUT_FILE = "../dataset/claims.csv"
OUTPUT_FILE = "../output.csv"

df = pd.read_csv(INPUT_FILE)

results = []

for i, row in df.iterrows():
    claim_id = row.get("claim_id", i)

    conversation = str(row.get("claim_description", "")).lower()
    obj = str(row.get("object_type", "")).lower()

    decision = "supported"
    issue_type = "damage"
    severity = "medium"

    text = conversation + " " + obj

    if "car" in text or "vehicle" in text:
        part = "car_body"
    elif "laptop" in text or "computer" in text:
        part = "screen"
    elif "package" in text or "box" in text:
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

print("DONE OUTPUT!")
