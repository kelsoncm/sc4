from zipfile import ZipFile
from io import BytesIO, StringIO
from csv import DictReader


class FileNotFoundInZipError(FileNotFoundError):
    pass


def unzip_content(content, file_id=0, encoding='utf-8'):
    with ZipFile(BytesIO(content)) as zip_file:
        try:
            filename = file_id if type(file_id) == str else zip_file.filelist[file_id].filename
        except IndexError:
            raise FileNotFoundInZipError("Não existe arquivo no índice %d")
        try:
            with zip_file.open(filename) as zipped_file:
                binary_file_content = zipped_file.read()
            return binary_file_content if encoding is None else binary_file_content.decode(encoding)
        except KeyError:
            raise FileNotFoundInZipError("Não existe arquivo com o nome %s" % filename)


def unzip_csv_content(content, file_id=0, encoding='utf-8', **kwargs):
    csv_stream_content = StringIO(unzip_content(content, file_id, encoding))
    return [dict(row) for row in DictReader(csv_stream_content, **kwargs)]
