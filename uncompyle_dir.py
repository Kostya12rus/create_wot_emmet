import os
import pathlib
import subprocess
from concurrent.futures import ThreadPoolExecutor
from tqdm import tqdm


def __decompile_file(file, new_file):
    try:
        subprocess.call(["uncompyle6", "-o", new_file, file], stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=30)
    except subprocess.TimeoutExpired:
        pass


def decompile_dir(dir_wot_pak: pathlib.Path, count_thread=10):
    pyc_files = [os.path.join(dir_path, filename) for dir_path, _, filenames in os.walk(dir_wot_pak) for filename in filenames if filename.endswith('.pyc')]
    progress = tqdm(desc='Декомпиляция файлов', total=len(pyc_files), unit='файлов')
    def thread_done_callback(future):
        progress.update()
    with ThreadPoolExecutor(max_workers=count_thread) as executor:
        for pyc_file in pyc_files:
            original_filepath = pyc_file[:-1]
            future = executor.submit(__decompile_file, pyc_file, original_filepath)
            future.add_done_callback(thread_done_callback)


def remove_pyc_file(dir_wot_pak: pathlib.Path):
    pyc_files = [os.path.join(dir_path, filename) for dir_path, _, filenames in os.walk(dir_wot_pak) for filename in filenames if filename.endswith('.pyc')]
    progress = tqdm(pyc_files, f"Удаление файлов .pyc", total=len(pyc_files), unit='файлов')
    for filenames in progress:
        os.remove(filenames)
    progress.close()
