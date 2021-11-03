import os, subprocess
from tqdm import tqdm
from threading import Thread

def __decompile_file(file, new_file):
    subprocess.call(f'uncompyle6 -o {new_file} {file}', stdout=subprocess.PIPE, stderr=subprocess.PIPE)

def decompile_dir(dir_wot_pak, count_thread=10):
    total = 0
    for dir_path, _, filenames in os.walk(dir_wot_pak):
        for filename in filenames:
            if filename.find('.pyc') > -1:
                total += 1
    all_thread = []
    progress = tqdm(os.walk(dir_wot_pak), f"Декодирование файлов", total=total, unit='файлов')
    for dir_path, _, filenames in progress.iterable:
        for filename in filenames:
            while True:
                for thread in all_thread.copy():
                    if not thread.is_alive():
                        all_thread.pop(all_thread.index(thread))
                if len(all_thread) < count_thread:
                    break
            if filename.find('.pyc') > -1:
                file_path = os.path.join(dir_path, filename)
                original_filename = filename.split('.')[0]
                original_filepath = dir_path + '/' + original_filename + '.py'
                thread = Thread(target=__decompile_file, args=(file_path, original_filepath,), daemon=True)
                thread.start()
                all_thread.append(thread)
                progress.update()
    progress.close()

def remove_pyc_file(dir_wot_pak):
    total = 0
    for dir_path, _, filenames in os.walk(dir_wot_pak):
        for filename in filenames:
            if filename.find('.pyc') > -1:
                total += 1
    progress = tqdm(os.walk(dir_wot_pak), f"Удаление файлов .pyc", total=total, unit='файлов')
    for dir_path, _, filenames in progress.iterable:
        for filename in filenames:
            if filename.find('.pyc') > -1:
                os.remove(os.path.join(dir_path, filename))
                progress.update()
    progress.close()