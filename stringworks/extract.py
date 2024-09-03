
email_id="sahal@gmail.com"

at_pos=email_id.index("@")

user_name=email_id[:at_pos]

print(user_name)

domain=email_id[at_pos:]

print(domain)