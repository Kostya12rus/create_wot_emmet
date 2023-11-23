import os
import pathlib
import subprocess
import time
import zipfile
import shutil
import uncompyle_dir

# Wargaming v.1.23.0.0 #311

thread_decode = 50  # Самое лучшее значение 20, чем выше, тем больше нагрузка на ЦП
# Процесор 4 ядра 8 потоков
# 25    420.78068s затрачено времени
# 50    425.95332s затрачено времени
# 100   425.08357s затрачено времени
# 150   423.97373s затрачено времени

# Процесор 24 ядра 48 потоков
# 25    223.18028s затрачено времени
# 50    181.12902s затрачено времени
# 100   197.27483s затрачено времени
# 150   202.98326s затрачено времени
# 200   205.09093s затрачено времени

time_start = time.time()
wot_path_pak = None
while True:
    _wot_path_str = input("Укажите путь папки с игрой: ").strip()
    wot_path = pathlib.Path(_wot_path_str)
    if not wot_path.is_dir():
        print("Указанной папки с игрой не существует")
        continue
    wot_path_pak = pathlib.Path(_wot_path_str + r"\res\packages\scripts.pkg")
    if not wot_path_pak.is_file():
        print("Файл scripts.pkg не найден в папке с игрой")
        continue
    break

local_pak_decode_path = pathlib.Path("wot_decode_files")
if local_pak_decode_path.is_dir():
    dir_del_time = time.time()
    shutil.rmtree(local_pak_decode_path, ignore_errors=True)
    print(f"{time.time() - dir_del_time:.5f}s удалена старая папка скриптов")
local_pak_decode_path.mkdir()

try:
    with zipfile.ZipFile(wot_path_pak, 'r') as z:
        zip_copy_time = time.time()
        z.extractall(local_pak_decode_path)
    print(f"{time.time() - zip_copy_time:.5f}s файлы scripts.pkg успешно перенесены")
except zipfile.BadZipFile as e:
    print("Ошибка разархивации файла scripts.pkg:", e)
    os.abort()
except Exception as e:
    print("Неизвестная ошибка при разархивации файла scripts.pkg:", e)
    os.abort()

decompile_time = time.time()
uncompyle_dir.decompile_dir(local_pak_decode_path, thread_decode)
print(f"{time.time() - decompile_time:.5f}s файлы декодированы")

remove_pyc_time = time.time()
uncompyle_dir.remove_pyc_file(local_pak_decode_path)
print(f"{time.time() - remove_pyc_time:.5f}s файлы .pyc удалены")

client_dir = local_pak_decode_path / 'scripts' / 'client'
client_common_dir = local_pak_decode_path / 'scripts' / 'client_common'
common_dir = local_pak_decode_path / 'scripts' / 'common'


emmet_dir = pathlib.Path('Emmets')
if emmet_dir.is_dir():
    dir_del_time = time.time()
    shutil.rmtree(emmet_dir, ignore_errors=True)
    print(f"{time.time() - dir_del_time:.5f}s удалена старая папка emmets")
emmet_dir.mkdir()

copy_time = time.time()
subprocess.call(['XCOPY', client_dir / "*.*", emmet_dir / "*.*", '/H', '/Y', '/C', '/R', '/S', '/Q'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
subprocess.call(['XCOPY', client_common_dir / "*.*", emmet_dir / "*.*", '/H', '/Y', '/C', '/R', '/S', '/Q'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
subprocess.call(['XCOPY', common_dir / "*.*", emmet_dir / "*.*", '/H', '/Y', '/C', '/R', '/S', '/Q'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(f"{time.time() - copy_time:.5f}s emmet создан")
print(f"{time.time() - time_start:.5f}s затрачено времени")
