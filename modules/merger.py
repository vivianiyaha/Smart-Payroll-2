import pandas as pd

def normalize_name(name):
    if pd.isna(name):
        return ""
    return str(name).strip().upper()

def merge_payroll(dfs, duplicate_rule="sum"):
    merged = {}

    for df in dfs:
        df["STAFF NAME"] = df["STAFF NAME"].apply(normalize_name)

        for _, row in df.iterrows():
            name = row["STAFF NAME"]
            if not name:
                continue

            if name not in merged:
                merged[name] = {}

            for col in df.columns:
                if col == "STAFF NAME":
                    continue

                value = row[col] if not pd.isna(row[col]) else 0
                merged[name][col] = merged[name].get(col, 0)

                if duplicate_rule == "sum":
                    merged[name][col] += value
                elif duplicate_rule == "first":
                    if merged[name][col] == 0:
                        merged[name][col] = value
                elif duplicate_rule == "last":
                    merged[name][col] = value

    return pd.DataFrame.from_dict(merged, orient="index").reset_index().rename(columns={"index": "STAFF NAME"})
