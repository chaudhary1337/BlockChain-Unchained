import json
from Person import Person

def make_people_pair(save=True):
    """
    Generates two peeps with each having valid keys.
    """  
    A = Person()
    B = Person()

    A_dump = json.dumps({'public_key': A.public_key, 'private_key': A.private_key}, indent=4)
    B_dump = json.dumps({'public_key': B.public_key, 'private_key': B.private_key}, indent=4)

    if save:
        with open('test_subject1.json', 'w') as f:
            f.write(A_dump)

        with open('test_subject2.json', 'w') as f:
            f.write(B_dump)

def import_people():
    with open('test_subject1.json', 'r') as f:
        A_data = json.load(f)
    
    with open('test_subject2.json', 'r') as f:
        B_data = json.load(f)

    A = Person(generate=False, debug=False, data=A_data)
    B = Person(generate=False, debug=False, data=B_data)

    return A, B

def text(text_from, text_to, message):
    commons = {
        f"{text_from}_public_key": text_from.public_key,
        f"{text_to}_public_key": text_to.public_key
    }

    encrypted_message = text_from.encrypt(commons[f'{text_to}_public_key'], message)
    # print(encrypted_message)
    print(text_to.decrypt(encrypted_message))

A, B = import_people()
message = int(input("Enter Message: "))
text(B, A, message)