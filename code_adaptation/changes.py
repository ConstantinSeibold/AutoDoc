from ollama import chat
from ollama import ChatResponse
from .extract_document import extract_text
from utils.files import get_file_extension
from tqdm import tqdm
from typing import List
import os


prompts = {
    "all": open("./prompt/all.txt").read(),
    "comments": open("./prompt/comments.txt").read(),
    "linting": open("./prompt/linting.txt").read(),
    "docstring": open("./prompt/docstring.txt").read(),
    "typehinting": open("./prompt/typehinting.txt").read(),
}

ignore_files = [
    ".txt",
    ".json"
    ".md"
]

def process_files(files: List[str], options: List[str], model_name: str):
    """
    Function/Method Description: The `process_files` function processes a list of files using specified options and runs them through a language model.
    Parameters:
        files (List[str]): A list of filenames to be processed.
        options (List[str]): A list of option names that define the tasks or transformations to apply to each file.
        model_name (str): The name of the language model to use for processing.
    Returns:
        None
    Example:
        >>> process_files(["file1.txt", "file2.txt"], ["linting", "docstring"], "gpt-4")
    Notes:
        This function uses the `tqdm` library for progress bars, which you can install using pip: `pip install tqdm`.
    """
    with tqdm(files, desc="Processing", dynamic_ncols=True) as pbar:
        for file in pbar:
            if not get_file_extension(file) in ignore_files:
                pbar.set_description(f"Processing: {file}")
                change_code(file, options, model_name)



def change_code(path_to_code: str, options: List[str], model_name: str):
    """
    Function/Method Description: The `change_code` function reads the content of a file, applies specified options, and writes the result back to the same file.
    Parameters:
        path_to_code (str): The path to the file whose code needs to be changed.
        options (List[str]): A list of option names that define the tasks or transformations to apply to the code.
        model_name (str): The name of the language model to use for applying the changes.
    Returns:
        None
    Example:
        >>> change_code("example.txt", ["linting", "docstring"], "gpt-4")
    """
    for option in options:
        print(f"Running {option}")
        try:
            apply_option(path_to_code, option, model_name)
        except Exception as e:
            print(e)



def apply_option(path_to_code: str, option: str, model_name: str):
    """
    Function/Method Description: The `apply_option` function applies a specific option to a file using a language model.
    Parameters:
        path_to_code (str): The path to the file whose code needs to be changed.
        option (str): The name of the option that defines the task or transformation to apply.
        model_name (str): The name of the language model to use for applying the changes.
    Returns:
        None
    Example:
        >>> apply_option("example.txt", "docstring", "gpt-4")
    Notes:
        This function uses the `chat` and `extract_text` functions from a hypothetical library or module.
    """
    init_prompt = prompts[option]
    code = open(path_to_code).read()
    prompt = init_prompt + "\n" + code
    
    response: ChatResponse = chat(model=model_name, messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])

    new_code: str = extract_text(response.message.content)
    
    with open(path_to_code, "w") as file:
        file.write(new_code)  # Write to the same file