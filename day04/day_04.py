import re


def validate_birth_year(year):
    year_int = int(year)
    min_birth_year = 1920
    max_birth_year = 2002
    is_valid = min_birth_year <= year_int <= max_birth_year
    return is_valid


def validate_issue_year(year):
    year_int = int(year)
    min_issue_year = 2010
    max_issue_year = 2020
    is_valid = min_issue_year <= year_int <= max_issue_year
    return is_valid


def validate_expiration_year(year):
    year_int = int(year)
    min_expiration_year = 2020
    max_expiration_year = 2030
    is_valid = min_expiration_year <= year_int <= max_expiration_year
    return is_valid


def validate_height(height):
    min_height_cm = 150
    max_height_cm = 193
    min_height_in = 59
    max_height_in = 76

    split_num_and_unit = re.findall(r'^(?P<numbers>\d*)(?P<letters>\w*)$', height)
    num = int(split_num_and_unit[0][0])
    unit = split_num_and_unit[0][1]

    if unit == 'cm':
        return min_height_cm <= num <= max_height_cm

    elif unit == 'in':
        return min_height_in <= num <= max_height_in
    else:
        return False


def validate_passport_id(passport_id):
    valid_passport_id = re.compile('[0-9]{9}')
    is_valid = bool(re.search(valid_passport_id, passport_id))
    return is_valid


def validate_hair_color(hair_color):
    valid_hair_color = re.compile('^#[0-9a-f]{6}')
    is_valid = bool(re.search(valid_hair_color, hair_color))
    return is_valid


def validate_eye_color(eye_color):
    valid_eye_color = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    is_valid = eye_color in valid_eye_color
    return is_valid


def validate_cid(cid):
    return True


def valid_passport_count(file_name):
    count = 0
    strict_count = 0
    num_fields = 0

    all_fields_valid = True
    cid_missing = True

    expected_fields = ['byr', 'iyr', 'eyr', 'hgt',
                       'hcl', 'ecl', 'pid', 'cid']

    validate = {
                'byr': validate_birth_year,
                'iyr': validate_issue_year,
                'eyr': validate_expiration_year,
                'hgt': validate_height,
                'hcl': validate_hair_color,
                'ecl': validate_eye_color,
                'pid': validate_passport_id,
                'cid': validate_cid
                }

    with open(file_name, 'r') as file:
        for line in file:
            if line != '\n':
                fields = line.split(' ')
                num_fields += len(fields)

                for field in fields:
                    if field.find('cid') != -1:
                        cid_missing = False

                    field = field.replace('\n', '')
                    split_field = field.split(':')

                    if all_fields_valid:
                        key = split_field[0]
                        value = split_field[1]
                        if key != 'cid':
                            valid_field = validate[key](value)

                        if not valid_field:
                            all_fields_valid = False

            elif line == '\n':
                only_missing_cid = cid_missing and (num_fields == 7)

                # All fields present
                if num_fields == len(expected_fields) or only_missing_cid:
                    count += 1
                    if all_fields_valid:
                        strict_count += 1

                num_fields = 0
                cid_missing = True
                all_fields_valid = True

        print(f'Passports with all required fields: {count}')
        print(f'Passports with all required fields and valid entry: {strict_count}')


def main():
    file = './input.txt'
    valid_passport_count(file)


if __name__ == "__main__":
    main()
