import sys
from pathlib import Path
import shutil
import re

import asyncio
import aiopath

import time

JPEG_IMAGES = []
JPG_IMAGES = []
PNG_IMAGES = []
SVG_IMAGES = []
AVI_VIDEOS = []
MP4_VIDEOS = []
MOV_VIDEOS = []
MKV_VIDEOS = []
DOC_DOCUMENTS = []
DOCX_DOCUMENTS = []
TXT_DOCUMENTS = []
PDF_DOCUMENTS = []
XLSX_DOCUMENTS = []
PPTX_DOCUMENTS = []
MP3_MUSICS = []
OGG_MUSICS = []
WAV_MUSICS = []
AMR_MUSICS = []
OTHER = []
ARCH = []
FOLDERS = []
UNKNOWN = set()
EXTENSION = set()

REGISTERED_EXTENSIONS = {
    "JPEG": JPEG_IMAGES,
    "JPG": JPG_IMAGES,
    "PNG": PNG_IMAGES,
    "SVG": SVG_IMAGES,
    "ZIP": ARCH,
    'AVI': AVI_VIDEOS,
    'MP4': MP4_VIDEOS,
    'MOV': MOV_VIDEOS,
    'MKV': MKV_VIDEOS,
    'DOC': DOC_DOCUMENTS,
    'DOCX': DOCX_DOCUMENTS,
    'TXT': TXT_DOCUMENTS,
    'PDF': PDF_DOCUMENTS,
    'XLSX': XLSX_DOCUMENTS,
    'PPTX': PPTX_DOCUMENTS,
    'MP3': MP3_MUSICS,
    'OGG': OGG_MUSICS,
    'WAV': WAV_MUSICS,
    'AMR': AMR_MUSICS
}

CYRILLIC_SYMBOLS = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяєіїґ'
TRANSLATION = ("a", "b", "v", "g", "d", "e", "e", "j", "z", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "u",
               "f", "h", "ts", "ch", "sh", "sch", "", "y", "e", "u", "ja")

TRANS = {}

for cs, trl in zip(CYRILLIC_SYMBOLS, TRANSLATION):
    TRANS[ord(cs)] = trl
    TRANS[ord(cs.upper())] = trl.upper()


def normalize(name: str) -> str:
    trl_name = name.translate(TRANS)
    trl_name = re.sub(r"\W", "_", trl_name)
    return trl_name


def get_extension(file_name) -> str:
    return Path(file_name).suffix[1:].upper()


async def scan(folder: Path):
    folder = aiopath.AsyncPath(folder)
    async for item in folder.iterdir():
        is_folder = await item.is_dir()
        if is_folder:
            if item.name not in REGISTERED_EXTENSIONS.keys():
                FOLDERS.append(item)
                await scan(item)
            continue

        extension = get_extension(item.name)
        new_name = folder / item.name
        if not extension:
            OTHER.append(new_name)
        else:
            try:
                current_container = REGISTERED_EXTENSIONS[extension]
                EXTENSION.add(extension)
                current_container.append(new_name)
            except KeyError:
                UNKNOWN.add(extension)
                OTHER.append(new_name)


async def handle_file(file: Path, root_folder: Path, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    if dist == "ARCH":
        folder_for_arch = normalize(file.name.replace(ext, ""))
        archive_folder = target_folder / folder_for_arch
        archive_folder.mkdir(exist_ok=True)  # create folder ARCH/name_archives
        try:
            shutil.unpack_archive(file, archive_folder)

        except shutil.ReadError:
            archive_folder.rmdir()
            return
        await file.unlink()
    else:
        new_name = normalize(file.name.replace(ext, "")) + ext
        await file.replace(target_folder / new_name)


async def handle_folder(folder: Path):
    try:
        await folder.rmdir()
    except OSError:
        print(f"Не удалось удалить папку {folder}")


async def main(folder):
    await scan(folder)

    # for items in REGISTERED_EXTENSIONS.values():
    #     for file in items:
    #         folder_new = list(REGISTERED_EXTENSIONS.keys())[list(REGISTERED_EXTENSIONS.values()).index(items)]
    #         await handle_file(file, folder, folder_new)


    for file in JPEG_IMAGES:
        await handle_file(file, folder, "JPEG")

    for file in JPG_IMAGES:
        await handle_file(file, folder, "JPG")

    for file in PNG_IMAGES:
        await handle_file(file, folder, "PNG")

    for file in SVG_IMAGES:
        await handle_file(file, folder, "SVG")

    for file in AVI_VIDEOS:
        await handle_file(file, folder, "AVI")

    for file in MP4_VIDEOS:
        await handle_file(file, folder, "MP4")

    for file in MOV_VIDEOS:
        await handle_file(file, folder, "MOV")

    for file in MKV_VIDEOS:
        await handle_file(file, folder, "MKV")

    for file in DOC_DOCUMENTS:
        await handle_file(file, folder, "DOC")

    for file in DOCX_DOCUMENTS:
        await handle_file(file, folder, "DOCX")

    for file in TXT_DOCUMENTS:
        await handle_file(file, folder, "TXT")

    for file in PDF_DOCUMENTS:
        await handle_file(file, folder, "PDF")

    for file in XLSX_DOCUMENTS:
        await handle_file(file, folder, "XLSX")

    for file in PPTX_DOCUMENTS:
        await handle_file(file, folder, "PPTX")

    for file in MP3_MUSICS:
        await handle_file(file, folder, "MP3")

    for file in OGG_MUSICS:
        await handle_file(file, folder, "OGG")

    for file in WAV_MUSICS:
        await handle_file(file, folder, "WAV")

    for file in AMR_MUSICS:
        await handle_file(file, folder, "AMR")

    for file in OTHER:
        await handle_file(file, folder, "OTHER")

    for file in ARCH:
        await handle_file(file, folder, "ARCH")

    for f in FOLDERS:
        await handle_folder(f)


if __name__ == "__main__":
    scan_path = sys.argv[1]
    print(f"Start in folder {scan_path}")
    sort_folder = Path(scan_path)
    print(sort_folder)
    print(sort_folder.resolve())
    asyncio.run(main(sort_folder.resolve()))
