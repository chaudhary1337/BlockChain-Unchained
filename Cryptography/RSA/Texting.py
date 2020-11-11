import json
from Person import Person

def make_people_pair(save=True):
    """
    Generates two peeps with each having valid keys.
    """
    global A
    global B
    
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
    global A
    global B
    
    with open('test_subject1.json', 'r') as f:
        A_data = json.load(f)
    
    with open('test_subject2.json', 'r') as f:
        B_data = json.load(f)

    A = Person(generate=False, debug=False, data=A_data)
    B = Person(generate=False, debug=False, data=B_data)

def text():
    import_people()

    commons = {
        "A_public_key": A.public_key,
        "B_public_key": B.public_key
    }

    encrypted_message = A.encrypt(commons['B_public_key'], message=42)
    print(encrypted_message)
    print(B.decrypt(encrypted_message))

text()