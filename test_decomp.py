import pathlib, os
import subprocess
import zipfile

from tqdm import tqdm
import uncompyle6
from threading import Thread

_wot_path_str = None
wot_path = None
wot_path_pak = None
while _wot_path_str is None:
    _wot_path_str = input("Укажите путь папки с игрой: ")
    wot_path = pathlib.Path(_wot_path_str)
    if not wot_path.is_dir():
        print("Указанной папки с игрой не существует")
        _wot_path_str = None
        continue
    wot_path_pak = pathlib.Path(_wot_path_str + r"\res\packages\scripts.pkg")
    if not wot_path_pak.is_file():
        print("Файл scripts.pkg не найден в папке с игрой")
        _wot_path_str = None
        continue

_local_pak_decode_path_str = "wot_decode_files"
local_pak_decode_path = pathlib.Path(_local_pak_decode_path_str)
if not local_pak_decode_path.is_dir():
    local_pak_decode_path.mkdir()

temp_file_dir = local_pak_decode_path / 'temp'
if not temp_file_dir.is_dir():
    temp_file_dir.mkdir()

try:
    if zipfile.ZipFile(wot_path_pak):
        with zipfile.ZipFile(wot_path_pak, 'r') as z:
            z.extractall(temp_file_dir)
except:
    print("Ошибка разархивации файла scripts.pkg")

def decompile_file(file, new_file):
    try:
        with open(new_file, 'w') as f:
            uncompyle6.decompile_file(file, f)
    except:
        pass

total = 0
for dir_path, _, filenames in os.walk(temp_file_dir):
    for filename in filenames:
        if filename.find('.pyc') > -1:
            total += 1


progress = tqdm(os.walk(temp_file_dir), f"Декодирование файлов", total=total, unit='файлов')
for dir_path, _, filenames in progress.iterable:
    for filename in filenames:
        if filename.find('.pyc') > -1:
            file_path = os.path.join(dir_path, filename)
            original_filename = filename.split('.')[0]
            original_filepath = dir_path + '/' + original_filename + '.py'
            # t = Thread(target=decompile_file, args=(file_path, original_filepath, ), daemon=True)
            # t.start()
            # all_thread.append(t)
            try:
                with open(original_filepath, 'w') as f:
                    uncompyle6.decompile_file(file_path, f)
            except:
                pass
            progress.update()
progress.close()
# uncompyle6 .\wot_decode_files/test




