def conversion(name, output_file):
    with open(name, "r") as file:
        first_data = file.read().split('\n')  # составление списка элементов, разделенных по \n
        massive = {}
        day = ''
        place = -1
        for i in first_data:
            j = i.strip()
            if j.count(':') == 1:
                key, value = j.split(':')
                if '-' not in key and len(value) == 0:  # при отсутствии "-" и значения после ":" парсер понимает, что это день
                    massive[key] = []
                    day = key  # значение дня присваивается day
                elif '-' in key:  # при присутствии "-" парсер понимает, что это занятие
                    lesson = key.strip("- ")
                    massive[day].append({lesson: {}})  # к ключу day добавляется словарь lesson с пока что пустым значением ключа {}
                    place += 1  # номер занятия увеличивается по мере исполнения кода, чтобы обращаться к нему дальше
                    place_name = lesson
                else:
                    value = value.strip()
                    massive[day][place][place_name][key] = value
            elif j.count(':') == 3:  # отдельный случай для времени
                key, time = j.split()
                key = key[:-1]
                value = time
                massive[day][place][place_name][key] = value
    spaces = 2
    with open(output_file, "w") as file2:
        number = 0
        file2.write("{\n")  # в начале файла всегда пишется }
        file2.write(spaces * ' ' + '"' + day + '": [\n')  # так как изначально dict
        spaces += 2
        file2.write(spaces * ' ' + "{\n")
        spaces += 2
        for i in massive[day]:
            for key1 in i.keys():
                file2.write(spaces * ' ' + '"' + key1 + '": {\n')
                lesson_now = massive[day][number][key1]  # обращение к конкретному занятию
                number += 1
                spaces += 2
                for key2 in lesson_now.keys():
                    file2.write(spaces * ' ' + '"' + key2 + '": ')  # проходим по всем признакам занятия
                    file2.write('"' + lesson_now[key2] + '", \n')
                spaces -= 2
                file2.write(spaces * ' ' + "}\n") 
                spaces -= 2
                file2.write(spaces * ' ' + "},\n")
                file2.write(spaces * ' ' + "{\n")
                spaces += 2

