import csv
import datetime


def convert_str_to_datetime(datetime_str):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strptime(datetime_str, "%d/%m/%Y %H:%M")


def convert_datetime_to_str(datetime_obj):
    """
    Конвертирует строку с датой в формате 11/10/2019 14:05 в объект datetime.
    """
    return datetime.datetime.strftime(datetime_obj, "%d/%m/%Y %H:%M")


def write_last_log_to_csv(source_log, output=None):
    with open(source_log) as f:
        reader = csv.reader(f)
        headers = next(reader)
        print('Headers: ', headers)
        unique_email = []
        result = []
        list_reader = list(reader)

        f.seek(2)
        for row in reader:
            if row[1] not in unique_email:
                arr_email = []
                unique_email.append(row[1])
                current_email = row[1]
                for line in list_reader:
                    if line[1] == current_email:
                        arr_email.append(line)
                if (arr_email == []):
                    continue
                else:
                    max = convert_str_to_datetime(arr_email[0][2])
                    result_max = arr_email[0]
                    for line in arr_email:
                        if max < convert_str_to_datetime(line[2]):
                            result_max = line
                            max = convert_str_to_datetime(line[2])
                    result.append(result_max)
        # print(unique_email)
        # print(result)
    with open(output, 'w') as g:
        writer = csv.writer(g)
        writer.writerow(headers)
        writer.writerows(result)


write_last_log_to_csv('mail_log.csv', 'log_output.csv')
