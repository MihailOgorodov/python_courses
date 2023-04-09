phone_book = []
start_phone_book = []

PATH = 'phone_book.txt'


def get_pb():
    return phone_book


def load_file():
    global start_phone_book
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for contact in data:
        contact = contact.strip().split(';')
        phone_book.append({'name': contact[0],
                           'phone': contact[1],
                           'comment': contact[2]})
    start_phone_book = phone_book.copy()


def safe_file():
    data = []
    for contact in phone_book:
        data.append(';'.join([value for value in contact.values()]))
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)


def add_contact(contact: dict):
    phone_book.append(contact)


def find_contact(word: str) -> list[dict[str, str]]:
    result = []
    for contact in phone_book:
        for field in contact.values():
            if word in field:
                result.append(contact)
                break
    return result


def edit_contact(edited_contact: tuple[int, dict[str, str]]) -> None:
    index, contact = edited_contact
    original_contact = phone_book.pop(index-1)
    contact = {'name': contact.get('name') if contact.get('name') else original_contact.get('name'),
               'phone': contact.get('phone') if contact.get('phone') else original_contact.get('phone'),
               'comment': contact.get('comment') if contact.get('comment') else original_contact.get('comment')}
    phone_book.insert(index-1, contact)

def delete_contact(index: int) -> str:
    deleted_element = phone_book.pop(index-1)
    return deleted_element.get('name')



def exit_pb() -> bool:
    if phone_book == start_phone_book:
        return False
    else:
        return True
