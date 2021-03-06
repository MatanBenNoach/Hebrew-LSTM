import codecs
import os

test_file_chars_count = 100000
input_folder = "Input"
output_file_train = "train.txt"
output_file_test = "test.txt"

chars = {}
chars_count = 0
my_text = ""
usable_chars = [' ', 'ו', 'י', 'ה', 'מ', 'ל', 'א', 'ר', 'ב', 'נ', 'ת', 'ש', 'ע', 'כ', ',', 'ד', '.', 'ח', 'פ', 'ק', '-',
                'צ', 'ג', 'ס', 'ז', '"', 'ט', '?', '!', ':', '\'', '\n','ן', 'ם', 'ף', 'ך', 'ץ']

for file in os.listdir(input_folder):
    if file.endswith(".txt"):
        file_path = os.path.join(input_folder, file)
        read_file_handler = codecs.open(file_path, "r", "utf-8")
        content = read_file_handler.readlines()
        read_file_handler.close()

        for line in content:
            line = line.replace(' ', ' ')
            line = line.replace('\r\n', u'\n')
            line = line.replace('\r', u'\n')
            for char in line:
                # Non-striped chars
                char = 'א' if char in ('א', 'אָ') else char
                char = 'ש' if char in ('ש', 'שׁ') else char
                char = 'ו' if char in ('ו', 'וּ', 'וֹ') else char

                # Similar chars
                char = "," if char in (",", ";") else char
                char = "'" if char in ("'", "'", "′") else char
                char = '-' if char in ('־', '-', '–', '─', '—', '­', '־', '‑') else char

                # Skip non usable chars
                if char not in usable_chars:
                    continue

                if char in chars:
                    chars[char] += 1
                else:
                    chars[char] = 1

                chars_count += 1

                # Collect char
                my_text += char

sorted_chars = sorted(chars, key=chars.get, reverse=True)
total = 0;
for char in sorted_chars:
    percent = int(chars[char])
    percent /= chars_count
    percent *= 100
    total += percent
    print("'" + str(char) + "':\t" + str(percent))

print(total)
print(chars_count)

train = my_text[test_file_chars_count:]
test = my_text[:test_file_chars_count]
write_file_handler = open(output_file_train, 'w', encoding="utf-8")
write_file_handler.write(train)
write_file_handler.close()

write_file_handler = open(output_file_test, 'w', encoding="utf-8")
write_file_handler.write(test)
write_file_handler.close()