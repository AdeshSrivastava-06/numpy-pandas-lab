import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Simple written dataset
data = {
    "Student": ["A","B","C","D","E","F","G","H","I","J"],
    "Math_Score": [55, 60, 65, 70, 72, 75, 78, 80, 85, 90]
}

df = pd.DataFrame(data)

#basic kde
sns.kdeplot(data=df, x="Math_Score", fill=True, color="blue")

plt.title("Density plot of maths score")
plt.xlabel("Score")
plt.ylabel("Density")
plt.show()

#little advanced
data = {
    "Student": ["A","B","C","D","E","F","G","H","I","J"],
    "Math_Score": [55, 60, 65, 90, 72, 75, 78, 80, 85, 90],
    "Science_Score": [58, 62, 94, 69, 71, 94, 76, 82, 87, 88]
}

df = pd.DataFrame(data)

plt.figure(figsize=(8,6))
#kde for maths
sns.kdeplot(data=df, x="Math_Score", fill=True, alpha=0.5, color="blue", label="Maths")
sns.kdeplot(data=df, x="Science_Score", fill=True, alpha=0.5, color="green", label="Science")

plt.title("Advanced KDE plot:Math vs science")
plt.xlabel("Score")
plt.ylabel("Density")
plt.legend()
plt.show()
