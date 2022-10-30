# %%
import pandas as pd
import numpy as np


# %%
def build_sheet_url(doc_id, sheet_id):
    return (
        "https://docs.google.com/spreadsheets/"
        f"d/{doc_id}/export?format=csv&gid={sheet_id}"
    )


# %%
x_col = "Actual Distance (limelight to hub center inches)"
y_col = "Flywheel RPM"

# %%
csv = pd.read_csv(
    build_sheet_url(
        doc_id="1HsdEImg3T0YNRP0I7jIUlTy6-clbWr-yfwyIP49YQmQ", sheet_id="2114529328"
    )
)

# %%
csv = csv[[x_col, y_col]].dropna()

# %%
java_code = csv.apply(
    lambda row: f"new SN_Point2D(Units.inchesToMeters({row[x_col]}), {row[y_col]}),",
    axis=1,
)

# %%

# %%
np.savetxt(r"out.txt", java_code.values, fmt="%s")

# %%
print(csv)

# %%
