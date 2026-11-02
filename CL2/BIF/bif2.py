import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = {
    "Gene": ["Gene1", "Gene2", "Gene3", "Gene4", "Gene5"],
    "Control": [100, 200, 150, 300, 100],
    "Treatment": [400, 50, 150, 600, 80],
    "Function": ["Growth", "Metabolism", "Repair", "Immunity", "Energy"]
}

df = pd.DataFrame(data)

print("RNA-Seq Dataset:")
print(df)

df["Fold Change"] = df["Treatment"] / df["Control"]

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
print((df["Status"].value_counts()))
print(
    "\nA full study should use replicate-aware tools "
    "such as DESeq2 or edgeR and adjust for multiple testing."
)
plt.bar(df["Status"].unique(),df["Status"].value_counts())
plt.title("conparing the RNA Status ")
plt.show()
