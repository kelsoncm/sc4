from csv import DictReader
from io import BytesIO, StringIO
from zipfile import ZipFile


class FileNotFoundInZipError(FileNotFoundError):
    pass


def unzip_content(content: bytes, file_id: int | str = 0, encoding: str = "utf-8") -> str | bytes:
    """Descompacta o conteúdo de um arquivo zip e retorna o conteúdo do arquivo especificado por file_id.
    Args:
        - content (bytes): O conteúdo do arquivo zip em formato de bytes.
        - file_id (int | str, optional): O índice ou nome do arquivo dentro do zip a ser descompactado.
            Padrão é 0 (primeiro arquivo).
        - encoding (str, optional): A codificação a ser usada para decodificar o conteúdo do arquivo.
            Se None, retorna bytes. Padrão é "utf-8".
    Returns:
        str | bytes: O conteúdo do arquivo descompactado, decodificado como string se encoding for
            especificado, ou como bytes se encoding for None.
    Raises:
        FileNotFoundInZipError: Se o arquivo especificado por file_id não for encontrado dentro do zip.
    """
    with ZipFile(BytesIO(content)) as zip_file:
        try:
            filename = file_id if isinstance(file_id, str) else zip_file.filelist[int(file_id)].filename
        except IndexError:
            raise FileNotFoundInZipError("Não existe arquivo no índice %d" % file_id)
        try:
            with zip_file.open(filename) as zipped_file:
                binary_file_content = zipped_file.read()
            return binary_file_content if encoding is None else binary_file_content.decode(encoding)
        except KeyError:
            raise FileNotFoundInZipError("Não existe arquivo com o nome %s" % filename)


def unzip_csv_content(content: bytes, file_id: int | str = 0, encoding: str = "utf-8", **kwargs) -> list[dict]:
    """Descompacta o conteúdo de um arquivo zip, lê o conteúdo do arquivo CSV especificado por file_id e retorna
    uma lista de dicionários representando as linhas do CSV.
    Args:
        - content (bytes): O conteúdo do arquivo zip em formato de bytes.
        - file_id (int | str, optional): O índice ou nome do arquivo CSV dentro do zip a ser descompactado.
            Padrão é 0 (primeiro arquivo).
        - encoding (str, optional): A codificação a ser usada para decodificar o conteúdo do arquivo CSV.
            Se None, retorna bytes. Padrão é "utf-8".
        - **kwargs: Argumentos adicionais a serem passados para csv.DictReader (como delimiter, quotechar, etc.).
    Returns:
        list[dict]: Uma lista de dicionários representando as linhas do CSV.
    """
    file_content = unzip_content(content, file_id, encoding)
    if not isinstance(file_content, str):
        file_content = file_content.decode(encoding) if isinstance(file_content, bytes) else str(file_content)
    csv_stream_content = StringIO(file_content)
    return [dict(row) for row in DictReader(csv_stream_content, **kwargs)]
