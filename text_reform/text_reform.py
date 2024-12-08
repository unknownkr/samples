import re


def remove_characters(value, characters):
    for char in characters:
        value = value.replace(char, '')
    return value


def select_numeric(value):
    # Use regular expression to extract numeric parts
    return ''.join(re.findall(r'\d+', str(value)))


def select_alpha_korean(value):
    # Use regular expression to extract alphabetic parts (Korean and English)
    return ''.join(re.findall(r'[가-힣a-zA-Z]+', str(value)))


def select_alphanumeric_korean(value):
    # Use regular expression to keep only numbers, Korean characters, and English letters
    return ''.join(re.findall(r'[0-9가-힣a-zA-Z]+', str(value)))


def reformat_bank_account(value):
    alpha_numeric = select_alphanumeric_korean(value)
    clean_str = remove_characters(alpha_numeric, ['은행', '계좌', '번호'])
    result = select_alpha_korean(clean_str) + select_numeric(clean_str)
    if value != result:
        print(f'Original: "{value}", Reformatted: "{result}"')


reformat_bank_account("국민은행 702101-04-009636")
reformat_bank_account("302ㅡ1288ㅡ6927ㅡ21")
reformat_bank_account("신한 61212230111 김가나")
reformat_bank_account("농협 3021269420321")
reformat_bank_account("기업은행 01053521280 김다라")


# Reformat room number
def format_room_number(value):
    pattern = r"([ABS])\D{0,5}0*([1-9]\d*)"
    value = value.upper()
    matches = re.findall(pattern, value)
    rooms = [f"{letter}{number}" for letter, number in matches]
    sorted_rooms = sorted(rooms, key=lambda x: (x[0], int(x[1:])))
    return ','.join(sorted_rooms)


rooms = ['B940', 'B1140b1542', 'B123 ~A~456', 'B1308', 'A동 01229호', 'B1425', 'B937', 'A910', 'A1312', 'B1140, B1542']
for room in rooms:
    reformed = format_room_number(room)
    if room != reformed:
        print(f'Original: {room}, Reformatted: {reformed}')


# Reformat phone number
def format_phone_number(value):
    numbers = ''.join(re.findall(r'\d+', str(value)))
    if len(numbers) == 10:
        return f'0{numbers[:2]}-{numbers[2:6]}-{numbers[6:]}'
    elif len(numbers) % 11 == 0:
        formatted_numbers = [f'{numbers[i:i + 3]}-{numbers[i + 3:i + 7]}-{numbers[i + 7:i + 11]}' for i in
                             range(0, len(numbers), 11)]
        return ','.join(formatted_numbers)
    return numbers
