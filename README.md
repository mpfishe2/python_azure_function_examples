# Python Azure Function Examples

This repository contains sample code for Python Azure Functions.  
  
What is in the repository:  
- `builderfunc`: this is just the boilerplate HTTP trigger in and HTTP response out for the Python Azure Function  
- `filereader`: this is a Python Azure Function with a Blob Trigger and a Event Hub output that can read blobs and send the content of the blobs as messages to the Event Hub  
  
## FileReader  
This function is currently built to parse PDFs and CSV documents.  
- For PDFs, it uses the PyPDF2 library and it extracts the fields of the PDF and formats them as a JSON object.  
- For CSVs it simply reads the blob into a Pandas DataFrame and then send back the first row as a comma-delimited string.  
  
### Planned Features  
- Improved PDF parsing with Azure Cognitive Services for OCR and Computer Vision  
- More file types for the purpose of having baseline examples for different types of files
  
## Instructions for VS Code  

1. Install the Azure Functions Extension for VS Code  
2. Install the Core Tools For Azure Functions  
3. Establish your Virtual Environment for Python using `venv` by running the following:  
  
**Command Prompt**  
```cmd
py -m venv .venv`  
`.venv\scripts\activate
```
**bash**  
```sh
python -m venv .venv
source .venv/bin/activate
```  
4. **If you want to start the function**: Go to the `__app__` directory and run:  
```sh
func start
```  
  
## Helpful Links for Python Azure Functions
1. [Python Function Reference](https://docs.microsoft.com/en-us/azure/azure-functions/functions-reference-python)  
2. [Good walkthrough for setting up a development environment for Python Functions](https://docs.microsoft.com/en-us/azure/azure-functions/functions-create-first-azure-function-azure-cli?tabs=bash%2Cbrowser&pivots=programming-language-python)  
3. [Fantastic Python Function Samples](https://docs.microsoft.com/en-us/samples/browse/?products=azure-functions&languages=python)
  
## Other Useful Notes about Az Functions  

### Trigger Tips  
For Event Grid, the webhook should be formatted like: https://{name_of_function_app}.azurewebsites.net/runtime/webhooks/eventgrid?functionName={name_of_function}&{function_key}  
  
### Publishing from VS Code Tips  
  
If you ever need to publish from a different tenant than the one that loads as the default tenant when you login into to Azure from the Azure Functions Extention blade, do the following:  
  
1. Go to Visual Studio Code Settings  
2. Search "Azure"  
3. In the left hand bar menu choose "Configuration"  
4. Enter the tenant/directory ID that you want it to login into (see picture below):  
5. Log in and you should now be in that context  
  
![Example Configuration](media\how_to_publish_function_to_different_tenant.png?raw=true "Example Configuration")