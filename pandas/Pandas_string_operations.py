import pandas as pd

data = {
    "name": ["  Amit Sharma", "priya PATEL", "Rohan verma  ", "SNEHA gupta"],
    "email": ["Amit@GMAIL.com", "priya123@yahoo.com", "rohan_v@gmail.com", "sneha@Hotmail.COM"],
    "phone": ["+91-9876543210", "9123456789", "+91 8765432109", "9988776655"],
}
df = pd.DataFrame(data)

print("original data:")
print(df)

# clean whitespace and fix casing
df["name"] = df["name"].str.strip().str.title()

# lowercase all emails
df["email"] = df["email"].str.lower()

# extract domain from email
df["email_domain"] = df["email"].str.split("@").str[1]

# keep only digits in phone numbers
df["phone_clean"] = df["phone"].str.replace(r"[^0-9]", "", regex=True)

# check if phone number contains a specific pattern
df["has_country_code"] = df["phone"].str.contains(r"\+91")

# get length of each name
df["name_length"] = df["name"].str.len()

print("\ncleaned data:")
print(df)

# filter rows where email domain is gmail
gmail_users = df[df["email_domain"].str.contains("gmail")]
print("\ngmail users only:")
print(gmail_users[["name", "email"]])
