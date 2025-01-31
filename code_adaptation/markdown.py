from ollama import chat
from ollama import ChatResponse
from utils.files import get_file_extension, get_files
from tqdm import tqdm
import os
from pathlib import Path


ignore_files = [
    ".txt",
    ".json"
    ".md"
]

prompts = {
    "markdown": open("./prompt/markdown_doc.txt").read(),
}

def doc_for_file(path_to_code, model_name: str, init_prompt):
    code = open(path_to_code).read()
    prompt = init_prompt + f"\n ```{path_to_code}" + code + "\n ```" 
    
    response: ChatResponse = chat(model=model_name, messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])

    documentation: str = response.message.content
    
    return documentation


def process_files_markdown(dir: str, model_name: str, suffix: str = 'py'):
    assert os.path.isdir(dir)
    files = get_files(dir, suffix)
    output_filename = f"{Path(dir).name}.md"
    output_path = os.path.join(dir, output_filename)
    
    init_prompt = prompts["markdown"]
    docs = ""
    with tqdm(files, desc="Processing", dynamic_ncols=True) as pbar:
        for file in pbar:
            if not get_file_extension(file) in ignore_files:
                prompt = init_prompt + f"\nDoc:{docs} \n\n\nCode:"
                doc = doc_for_file(file, model_name, prompt)
                docs += "\n "+ doc
    # Write the documentation to a Markdown file
    
    with open(output_path, 'w') as f:
        f.write(docs)

    print(f"Documentation written to {output_path}")