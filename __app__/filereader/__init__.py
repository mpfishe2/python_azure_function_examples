import azure.functions as func
import logging
import os
from azure.storage.blob import BlobClient
import __app__.shared_code.read_blob_content as read_blob_content

def main(blob: func.InputStream) -> str:
    # this would be defined in the local.settings.json and your Application Settings 
    CONN_STR = os.getenv("NAME_OF_CONNECTION_STRING_ENV")
    logging.info(f"\n\n"
                 f"------------------------------------------- \n"
                 f"Python blob trigger function processed blob \n"
                 f"Name: {blob.name}\n"
                 f"Blob Size: {blob.length} bytes\n"
                 f"Uri: {blob.uri} \n"
                 f"------------------------------------------- \n")
    # Get name of container
    containerName = (blob.name).split("/")[0]
    # Get the blob name
    adjblobName = (blob.name).split("/")[1]
    # Isolate the extension of the blob
    extensionOfBlob = adjblobName.split(".")[1]
    # Based on the extension of the blob, the function will choose which parser to use
    # NOTE: If you have a file extension explicitly defined in `function.json` then only that
    # file type will be processed. For example, container/{file}.csv will only trigger for CSVs
    blobContent = blob_file_parser(extensionOfBlob, CONN_STR, adjblobName, containerName)
    logging.info(blobContent)
    return blobContent