import argh
from services.generate import generate
from utils.file_menager import array_to_csv


def run(file_path, n, d=2, low=-1, high=1):
    p0 = generate(n, d, low, high)
    array_to_csv(file_path, p0)


if __name__ == '__main__':
    # argh.dispatch_command(run)
    run('files/test.csv', 100)  # for testing
