import json
from Person import Person

# A = Person(name="Apples")
# B = Person(name="Bananas")

# A_dump = json.dumps([A.public_key, A.private_key], indent=4)
# B_dump = json.dumps([B.public_key, B.private_key], indent=4)

# with open('A_test_subject.json', 'w') as f:
#     f.write(A_dump)

# with open('B_test_subject.json', 'w') as f:
#     f.write(B_dump)

# commons = {
#     "A_public_key": A.public_key,
#     "B_public_key": B.public_key
# }

# encrypted_message = A.encrypt(commons['B_public_key'], message=42)
# B.decrypt(encrypted_message)
# print(pow(42, B.public_key['e']*B.private_key['d'], B.public_key['n']))