
from argparse import ArgumentParser
from pathlib import Path
import json
import yaml

parser = ArgumentParser(
    prog="jaml",
    description="hoge"
)
parser.add_argument('filename', type=str, default=None, help='setting filename')


def jaml():
    args = parser.parse_args()
    path = Path(f'./{args.filename}')

    if path.suffix == '.json':
        with path.open(mode='r') as f:
            dic = json.load(f)
        with open(f"{path.stem}.yaml", "w") as yf:
            yaml.dump(dic, yf, default_flow_style=False)
    if path.suffix == '.yaml':
        with path.open(mode='r') as f:
            dic = yaml.load(f)
        with open(f"{path.stem}.json", "w") as jf:
            json.dump(dic, jf)


if __name__ == '__main__':
    jaml()
