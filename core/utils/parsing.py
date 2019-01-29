import sys, re, datetime

from core.models import ParsedData


def parsing():
    with open("/tmp/log_parser/access.log") as f:
        data = f.readlines()
        total = len(data)

        regex = r'(?P<remoteaddr>[\d\.]+) (?P<clientid>\S+) (?P<userid>\S+)' \
                r' \[(?P<timestamp>[^\]]+)\] \"(?P<request>[^\"]+)\" ' \
                r'(?P<status>\d+) (.*?) \"(.*?)\"' \
                r' \"(?P<useragent>[^\"]+).*'

        print('Всего строк {}. Начинаем импорт данных...'.format(total))
        if total is None:
            print('Ошибка чтения файла')
        else:
            for index, line in enumerate(data, start=1):
                # если строка не пустая
                if line and line.strip():
                    try:
                        parsed_line = re.match(regex, line).groups()
                    except:
                        # TODO повозиться ещё с парсингом url
                        # пока отбрасываю, а то не успеваю
                        pass
                    else:
                        ip_addr = parsed_line[0]
                        log_date = datetime.datetime.strptime(
                            parsed_line[3], "%d/%b/%Y:%H:%M:%S %z"
                        )
                        http_method = parsed_line[4].split(' ')[0]

                        if parsed_line[7] == "-":
                            uri = parsed_line[4].split(' ')[1]
                        else:
                            uri = parsed_line[7] + \
                                  parsed_line[4].split(' ')[1][1:]

                        error_code = int(parsed_line[5])

                        try:
                            response_size = int(parsed_line[6])
                        except:
                            response_size = 0

                        other = parsed_line[8]

                        # TODO переделать через bulk_create
                        ParsedData.objects.create(
                            ip_addr=ip_addr,
                            log_date=log_date,
                            http_method=http_method,
                            uri=uri,
                            error_code=error_code,
                            response_size=response_size,
                            other=other
                        )

                        # выводим прогресс бар
                        done = int(50 * index / total)
                        sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50 - done)))
                        sys.stdout.flush()
        sys.stdout.write('\n')

    return 0
