from ollama import chat
from ollama import ChatResponse
from .extract_document import extract_text
from tqdm import tqdm
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

def get_file_extension(filename):
    # Split the filename into base name and extension
    base_name, extension = os.path.splitext(filename)
    
    # Return the extension (excluding the dot)
    return extension

def process_files(files, options, model_name):
    with tqdm(files, desc="Processing", dynamic_ncols=True) as pbar:
        for file in pbar:
            if not get_file_extension(file) in ignore_files:
                pbar.set_description(f"Processing: {file}")  # This works
                change_code(file, options, model_name)


def change_code(path_to_code, options, model_name):
    for option in options:
        print(f"Running {option}")
        try:
            apply_option(path_to_code, option, model_name)
        except Exception as e:
            print(e)

def apply_option(path_to_code, option, model_name):
    
    init_prompt = prompts[option]
    code = open(path_to_code).read()
    prompt = init_prompt + "\n" + code
    
    response: ChatResponse = chat(model=model_name, messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])

    new_code = extract_text(response.message.content)
    
    with open(path_to_code, "w") as file:
        file.write(new_code)
    