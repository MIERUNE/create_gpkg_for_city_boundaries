import os
import re
import sys
import time
from concurrent.futures.thread import ThreadPoolExecutor
from pathlib import Path

import requests
from tqdm import tqdm


def main():
    """処理を実行します"""
    URL = "https://www.e-stat.go.jp/gis/statmap-search/data?dlserveyId=A002005212015&code={pref_code}&coordSys=1&format=shape&downloadType=5"

    download_dir = Path("../download")
    if not download_dir.exists():
        download_dir.mkdir()

    str_pref = [str(pref_code).zfill(2) for pref_code in range(1, 48)]
    args = [(URL.format(pref_code=p), download_dir.resolve()) for p in str_pref]
    with ThreadPoolExecutor(max_workers=3) as executor:
        executor.map(lambda p: download_file(*p), args)


def get_file_name_from_response(url, response):
    """responseのContent-Dispositionからファイル名を取得、できなければURLの末尾をファイル名として返す

    Args:
        url (str): リクエストのURL
        response (Response): responseオブジェクト

    Returns:
        str: ファイル名を返す

    """
    disposition = response.headers["Content-Disposition"]
    try:
        file_name = re.findall(r"filename.+''(.+)", disposition)[0]
    except IndexError:
        print("ファイル名が取得できませんでした")
        file_name = os.path.basename(url)
    return file_name


def download_file(url, dir_path, overwrite=True):
    """URLと保存先ディレクトリを指定してファイルをダウンロード

    Args:
        url (str): ダウンロードリンク
        dir_path (Path): 保存するディレクトリのパス文字列
        overwrite (bool): ファイル上書きオプション。Trueなら上書き

    Returns:
        Path: ダウンロードファイルのパスオブジェクト

    Notes:
        すでにファイルが存在していて、overwrite=Falseなら何もせず
        ファイルパスを返す

    """
    res = requests.get(url, stream=True)

    file_name = get_file_name_from_response(url, res)
    download_path = dir_path / file_name

    if download_path.exists() and not overwrite:
        print("ファイルがすでに存在し、overwrite=Falseなのでダウンロードを中止します。")
        return download_path

    # content-lengthは必ず存在するわけでは無いためチェック
    try:
        file_size = int(res.headers["content-length"])
    except KeyError:
        file_size = None
    progress_bar = tqdm(total=file_size, unit="B", unit_scale=True)

    if res.status_code == 200:
        print(f"{url=}, {res.status_code=}")
        print(f"{file_name}のダウンロードを開始します")
        with download_path.open("wb") as file:
            for chunk in res.iter_content(chunk_size=1024):
                file.write(chunk)
                progress_bar.update(len(chunk))
            progress_bar.close()
        return download_path
    else:
        print(f"{url=}, {res.status_code=}")
        print("正常にリクエストできませんでした。システムを終了します。")
        sys.exit(1)


if __name__ == "__main__":
    main()
