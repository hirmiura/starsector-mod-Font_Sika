#!/usr/bin/env -S python3
# SPDX-License-Identifier: MIT
# Copyright 2022 hirmiura <https://github.com/hirmiura>
from __future__ import annotations

import argparse
import io
import re
import sys

RE_MATCH_NAME = 'id'
CHAR_REX = re.compile(rf'^char\s+id=(?P<{RE_MATCH_NAME}>\d+)\s')


def pargs() -> None:
    global args
    parser = argparse.ArgumentParser(
        description='2つのfntファイルを比較して使用している文字コードの差を出力する')
    parser.add_argument('files', nargs=2, help='2つの入力ファイル')
    args = parser.parse_args()


def parse_file(file: str) -> set:
    assert file is not None
    ids = set()
    with open(file, 'r') as f:
        for line in f:
            match = CHAR_REX.match(line)
            if match:
                ids.add(int(match.group(RE_MATCH_NAME)))
    return ids


def process() -> None:
    lids = []
    for file in args.files:
        # print(f'{file} を処理中...', flush=True)
        ids = parse_file(file)
        lids.append(ids)
    # 和/差/共通
    add = lids[1] - lids[0]
    sub = lids[0] - lids[1]
    inter = lids[0] & lids[1]
    # 右寄せのための桁計算
    anum = len(add)
    snum = len(sub)
    inum = len(inter)
    astr = f'{anum:,}'
    sstr = f'{snum:,}'
    istr = f'{inum:,}'
    keta = (max(len(astr), len(sstr), len(istr)))
    # 結果表示
    print(f'追加: {astr: >{keta}}')
    print(f'削除: {sstr: >{keta}}')
    print(f'共通: {istr: >{keta}}')


def main():
    pargs()
    process()
    return 0


if __name__ == '__main__':
    # MSYS2での文字化け対策
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
    sys.exit(main())
