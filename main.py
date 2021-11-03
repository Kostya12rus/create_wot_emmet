import pathlib, os, time
import subprocess
import zipfile
import uncompyle_dir

time_start = time.time()
wot_path_pak = None
while wot_path_pak is None:
    _wot_path_str = input("Укажите путь папки с игрой: ").strip()
    wot_path = pathlib.Path(_wot_path_str)
    if not wot_path.is_dir():
        print("Указанной папки с игрой не существует")
        wot_path = None
        continue
    wot_path_pak = pathlib.Path(_wot_path_str + r"\res\packages\scripts.pkg")
    if not wot_path_pak.is_file():
        print("Файл scripts.pkg не найден в папке с игрой")
        wot_path_pak = None
        continue

local_pak_decode_path = pathlib.Path("wot_decode_files")
if local_pak_decode_path.is_dir():
    dir_del_time = time.time()
    while local_pak_decode_path.is_dir():
        subprocess.call(f'RMDIR /S /Q "{local_pak_decode_path}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(0.1)
    print('{:.5f}s'.format(time.time()-dir_del_time), 'удалена старая папка скриптов', )
local_pak_decode_path.mkdir()

try:
    if zipfile.ZipFile(wot_path_pak):
        zip_copy_time = time.time()
        with zipfile.ZipFile(wot_path_pak, 'r') as z:
            z.extractall(local_pak_decode_path)
        print('{:.5f}s'.format(time.time()-zip_copy_time), 'файлы scripts.pkg успешно перенесены')
except:
    print("Ошибка разархивации файла scripts.pkg")

decompile_time = time.time()
uncompyle_dir.decompile_dir(local_pak_decode_path, 20)
print('{:.5f}s'.format(time.time()-decompile_time), 'файлы декодированы')

remove_pyc_time = time.time()
uncompyle_dir.remove_pyc_file(local_pak_decode_path)
print('{:.5f}s'.format(time.time()-remove_pyc_time), 'файлы .pyc удалены')

client_dir = local_pak_decode_path / 'scripts' / 'client'
client_common_dir = local_pak_decode_path / 'scripts' / 'client_common'
common_dir = local_pak_decode_path / 'scripts' / 'common'

emmet_dir = pathlib.Path('Emmets')
if emmet_dir.is_dir():
    dir_del_time = time.time()
    while emmet_dir.is_dir():
        subprocess.call(f'RMDIR /S /Q "{emmet_dir}"', shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        time.sleep(0.1)
    print('{:.5f}s'.format(time.time()-dir_del_time), 'удалена старая папка emmets', )
emmet_dir.mkdir()

copy_time = time.time()
subprocess.call(fr'XCOPY "{client_dir.absolute()}\*.*" "{emmet_dir.absolute()}\*.*" /H /Y /C /R /S /Q', shell=True)
subprocess.call(fr'XCOPY "{client_common_dir.absolute()}\*.*" "{emmet_dir.absolute()}\*.*" /H /Y /C /R /S /Q', shell=True)
subprocess.call(fr'XCOPY "{common_dir.absolute()}\*.*" "{emmet_dir.absolute()}\*.*" /H /Y /C /R /S /Q', shell=True)
print('{:.5f}s'.format(time.time() - copy_time), 'emmet создан', )

print('{:.5f}s'.format(time.time()-time_start), 'затрачено времени')

# F:\World_of_Tanks_RU
