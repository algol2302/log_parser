import sys
import requests


def download(url, filename):
    with open(filename, 'wb') as f:
        response = requests.get(url, stream=True)
        total = response.headers.get('content-length')
        print('Начинаем загрузку файла {}'.format(url))
        if total is None:
            f.write(response.content)
        else:
            downloaded = 0
            total = int(total)
            for data in response.iter_content(
                    chunk_size=max(int(total/1000), 1024*1024)
            ):
                downloaded += len(data)
                f.write(data)
                done = int(50*downloaded/total)
                # прогресс бар самый простой
                # TODO можно использовать progress или tqdm
                sys.stdout.write('\r[{}{}]'.format('█' * done, '.' * (50-done)))
                sys.stdout.flush()
    sys.stdout.write('\n')

    return 0
