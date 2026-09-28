from password_generator import generate_password

print("Password Generator Test")
print("------------------------")

password = generate_password(10)

print("Generated Password:", password)

if len(password) == 10:
    print("Test Passed!")
else:
    print("Test Failed!")