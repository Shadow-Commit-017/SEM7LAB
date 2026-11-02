import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("rna_counts.csv")

control_cols = [col for col in df.columns if col.startswith("Control")]
treatment_cols = [col for col in df.columns if col.startswith("Treatment")]
df["Control"] = df[control_cols].mean(axis=1)
df["Treatment"] = df[treatment_cols].mean(axis=1)

df["FoldChange"] = df["Treatment"] / df["Control"]
df["Log2FC"] = np.log2(df["FoldChange"])


def classify(log2fc):
    if log2fc >= 1:
        return "Upregulated"
    elif log2fc <= -1:
        return "Downregulated"
    else:
        return "Not significant"

df["Status"] = df["Log2FC"].apply(classify)


print(
    df[["Gene","Control","Treatment","FoldChange","Log2FC","Status"]].to_string(index=False)
)
df["Status"].value_counts()
print(
    "\nA full study should use replicate-aware tools "
    "such as DESeq2 or edgeR and adjust for multiple testing."
)
plt.bar(df["Status"].unique(),df["Status"].value_counts())
plt.title("conparing the RNA Status ")
plt.show()
