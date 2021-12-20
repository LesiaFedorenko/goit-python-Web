import sys
from pathlib import Path
import shutil
import scan
from normalize import normalize
import concurrent.futures


def handle_file(file: Path, root_folder: Path, dist):
    target_folder = root_folder / dist
    target_folder.mkdir(exist_ok=True)
    ext = Path(file).suffix
    if dict == "ARCH":
        folder_for_arch = normalize(file.name.replace(ext, ""))
        archive_folder = target_folder / folder_for_arch
        archive_folder.mkdir(exist_ok=True)  # create folder ARCH/name_archives
        try:
            shutil.unpack_archive(str(file.resolve()), str(archive_folder.resolve()))
        except shutil.ReadError:
            archive_folder.rmdir()
            return
        file.unlink()
    else:
        new_name = normalize(file.name.replace(ext, "")) + ext
        file.replace(target_folder / new_name)

def handle_folder(folder: Path):
    try:
        folder.rmdir()
    except OSError:
        print(f"Не удалось удалить папку {folder}")


def main(folder):
    scan.scan(folder)
    for thread in scan.threads:
        thread.join()

    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        tuple_images = tuple(
            scan.JPEG_IMAGES + scan.JPG_IMAGES +scan.PNG_IMAGES + scan.SVG_IMAGES +
            scan.AVI_VIDEOS + scan.MP4_VIDEOS + scan.MOV_VIDEOS + scan.MKV_VIDEOS +
            scan.DOC_DOCUMENTS + scan.DOCX_DOCUMENTS +
            scan.TXT_DOCUMENTS + scan.PDF_DOCUMENTS +
            scan.XLSX_DOCUMENTS + scan.PPTX_DOCUMENTS +
            scan.MP3_MUSICS + scan.OGG_MUSICS + scan.WAV_MUSICS + scan.AMR_MUSICS)
        tuple_folder = tuple([folder] * len(tuple_images))
        tuple_name = tuple(
            ["JPEG"] * len(scan.JPEG_IMAGES) +
            ["JPG"] * len(scan.JPG_IMAGES) +
            ["PNG"] * len(scan.PNG_IMAGES) +
            ["SVG"] * len(scan.SVG_IMAGES) +
            ["AVI"] * len(scan.AVI_VIDEOS) +
            ["MP4"] *len(scan.MP4_VIDEOS) +
            ["MOV"] *len(scan.MOV_VIDEOS) +
            ["MKV"] * len(scan.MKV_VIDEOS) +
            ["DOC"] * len(scan.DOC_DOCUMENTS) +
            ["DOCX"] * len(scan.DOCX_DOCUMENTS) +
            ["TXT"] * len(scan.TXT_DOCUMENTS) +
            ["PDF"] * len(scan.PDF_DOCUMENTS) +
            ["XLSX"] * len(scan.XLSX_DOCUMENTS) +
            ["PPTX"] * len(scan.PPTX_DOCUMENTS) +
            ["MP3"] * len(scan.MP3_MUSICS) +
            ["OGG"] * len(scan.OGG_MUSICS) +
            ["WAV"] * len(scan.WAV_MUSICS) +
            ["AMR"] * len(scan.AMR_MUSICS))
        executor.map(handle_file, tuple_images, tuple_folder, tuple_name)

        for file in scan.OTHER:
            executor.submit(handle_file, file, folder, "OTHER")

        for file in scan.ARCH:
            executor.submit(handle_file, file, folder, "ARCH")

    print('End')
    for f in scan.FOLDERS:
        handle_folder(f)


if __name__ == "__main__":
    scan_path = sys.argv[1]
    print(f"Start in folder {scan_path}")

    sort_folder = Path(scan_path)
    print(sort_folder)
    print(sort_folder.resolve())
    main(sort_folder.resolve())
