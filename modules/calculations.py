def compute_salary(df):
    earnings_cols = ["BASIC", "HOUSING", "TRANSPORT"]
    deduction_cols = ["TAX", "PENSION", "LOAN", "SAL. ADV.", "PENALTY"]

    df["GROSS SALARY"] = df[earnings_cols].sum(axis=1, min_count=1)
    df["TOTAL DEDUCTIONS"] = df[deduction_cols].sum(axis=1, min_count=1)
    df["NET SALARY"] = df["GROSS SALARY"] - df["TOTAL DEDUCTIONS"]

    return df
