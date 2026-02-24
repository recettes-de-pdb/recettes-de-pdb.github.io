import pandas as pd
import os

# Ensure folders exist
os.makedirs("drive_data", exist_ok=True)

# Load CSV
df = pd.read_csv("data.csv")

# Example transformation
html_table = df.to_html(index=False)

# Generate website content
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Recettes</title>
</head>
<body>
    <h1>Recettes</h1>
    {html_table}
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Website updated successfully.")