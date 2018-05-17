from .config import config


def gen_load_rss_source():
    with open(config.SOURCE_FILE, 'r') as f:
        for line in f:
            if line:
                # remove '/n'
                yield line[:-1]


if __name__ == '__main__':
    for i in gen_load_rss_source():
        print(i)
