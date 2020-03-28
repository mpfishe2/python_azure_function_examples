import os
import io
import PyPDF2
import json
import time
import base64
import pandas as pd
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient


class Error(Exception):
    """Base class for other exceptions"""
    pass

class FileTypeNotSupported(Error):
    """Raised when a Smoke Test has failed"""
    pass

def blob_file_parser(extension, conn_str, blob_name, container_name):
    if "pdf" in extension:
        parse_pdf_blob(conn_str, blob_name, container_name)
    elif "csv" in extension:
        parse_csv_blob(conn_str, blob_name, container_name)
    else:
        logging.error(f"ERROR: File type {extension} not supported.")
        raise FileTypeNotSupported()


def parse_pdf_blob(conn_str, blob_name, container_name):
    blob_service_client = BlobServiceClient.from_connection_string(conn_str)
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    data = io.BytesIO(blob_client.download_blob().readall())
    pdfReader = PyPDF2.PdfFileReader(data)
    numOfPages = pdfReader.getNumPages()
    pageObj = pdfReader.getPage(numOfPages-1)
    pageFields = pdfReader.getFields()
    print(pageFields)
    pageText = pdfReader.getFormTextFields()
    return json.dumps(pageText)


#print(parse_pdf_blob("connection_string","name_of_pdf", "container_name"))



def parse_csv_blob(conn_str, blob_name, container_name):
    blob_service_client = BlobServiceClient.from_connection_string(conn_str)
    container_client = blob_service_client.get_container_client(container_name)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
    data = io.BytesIO(blob_client.download_blob().readall())
    # read into pandas DF
    df = pd.read_csv(data)
    logging.info(df)
    # return first row as string (to match the required dtype of the output of the function)
    csvData = df.to_csv(header=True, index=False).strip('\n').split('\n')
    return csvData[1]

#print(parse_csv_blob("connection_string","name_of_csv", "container_name"))