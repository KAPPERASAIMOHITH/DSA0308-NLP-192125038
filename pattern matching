import re
inputs = "Hello there! My name is John Smith and you can reach me at john.smith@example.com or call me at +1 (555) 123-4567. Alternatively, you can email me at j.smith@gmail.com. For urgent matters, please contact my assistant at assistant@example.com or call our office at 123456789
"
email = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
phone = r'\b[0-9]{10}\b'
emails = re.findall(email, inputs)
print("Email addresses found:", emails)
phones = re.findall(phone, inputs)
print("Phone numbers found:", phones)
