#!/usr/bin/env -S python3
# SPDX-License-Identifier: MIT
# Copyright 2022 hirmiura <https://github.com/hirmiura>
from __future__ import annotations

import argparse
import io
import re
import sys
import pathlib

RE_MATCH_NAME = 'id'
CHAR_REX = re.compile(rf'^char\s+id=(?P<{RE_MATCH_NAME}>\d+)\s')
NEW_SUFFIX = '.txt'


def pargs() -> None:
    global args
    parser = argparse.ArgumentParser(
        description='fntファイルから使用している文字コードを取り出してtxtファイルへ出力する')
    parser.add_argument('files', nargs='+', help='1つ以上の入力ファイル')
    args = parser.parse_args()


def parse_file(file: str) -> list[int]:
    assert file is not None
    ids = set()
    with open(file, 'r') as f:
        for line in f:
            match = CHAR_REX.match(line)
            if match:
                ids.add(int(match.group(RE_MATCH_NAME)))
    return sorted(ids)


def output_file(file: str, ids: list[int]) -> None:
    assert file is not None
    assert ids is not None
    text = ''
    for id in ids:
        text += chr(id)
    with open(file, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'==>{file} に {len(ids):,} 文字書き出し', flush=True)


def process() -> None:
    for file in args.files:
        print(f'{file} を処理中...', flush=True)
        ids = parse_file(file)
        newfile = pathlib.Path(file).with_suffix(NEW_SUFFIX)
        output_file(newfile, ids)


def main():
    pargs()
    process()
    return 0


if __name__ == '__main__':
    # MSYS2での文字化け対策
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    sys.exit(main())
