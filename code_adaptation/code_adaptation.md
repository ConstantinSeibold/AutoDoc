
 ## `changes.py`

### Description
The `changes.py` script is a utility for processing files using specified options and running them through a language model. It reads the content of each file, applies the specified transformations, and writes the result back to the same file.

### Usage
To run the script, you need to ensure that the necessary dependencies are installed. You can install these dependencies using pip:
```sh
pip install tqdm
```

Then, execute the script with the appropriate options and model name:
```sh
python changes.py --files "file1.txt" "file2.txt" --options "linting docstring" --model-name "gpt-4"
```

### Code Structure & Explanation

#### `process_files`
This function processes a list of files using specified options and runs them through a language model.

```markdown
##### process_files
The `process_files` function reads the content of each file, applies the specified transformations, and writes the result back to the same file.
```

- **Parameters:**
  - `files (List[str]): A list of filenames to be processed.`
  - `options (List[str]): A list of option names that define the tasks or transformations to apply to each file.`
  - `model_name (str): The name of the language model to use for processing.`

- **Returns:**
  - `None`

- **Example:**
  ```markdown
##### Example usage
```sh
python changes.py --files "file1.txt" "file2.txt" --options "linting docstring" --model-name "gpt-4"
```

#### `change_code`
This function reads the content of a file, applies specified options, and writes the result back to the same file.

```markdown
##### change_code
The `change_code` function reads the content of a file, applies the specified transformations, and writes the result back to the same file.
```

- **Parameters:**
  - `path_to_code (str): The path to the file whose code needs to be changed.`
  - `options (List[str]): A list of option names that define the tasks or transformations to apply to the code.`
  - `model_name (str): The name of the language model to use for applying the changes.`

- **Returns:**
  - `None`

- **Example:**
  ```markdown
##### Example usage
```sh
python changes.py --files "example.txt" --options "linting docstring" --model-name "gpt-4"
```

#### `apply_option`
This function applies a specific option to a file using a language model.

```markdown
##### apply_option
The `apply_option` function applies a specific option to a file using a language model.
```

- **Parameters:**
  - `path_to_code (str): The path to the file whose code needs to be changed.`
  - `option (str): The name of the option that defines the task or transformation to apply.`
  - `model_name (str): The name of the language model to use for applying the changes.`

- **Returns:**
  - `None`

- **Example:**
  ```markdown
##### Example usage
```sh
python changes.py --files "example.txt" --options "docstring" --model-name "gpt-4"
```

### Examples & Edge Cases

#### Example Usage
To run the script, execute the following command:
```sh
python changes.py --files "file1.txt" "file2.txt" --options "linting docstring" --model-name "gpt-4"
```

This will process `file1.txt` and `file2.txt`, applying linting and docstring transformations using the `gpt-4` language model. The script uses tqdm for progress bars, which you can install using pip: `pip install tqdm`.

#### Edge Cases
- **File Not Found**: If a file is not found, the script will raise an exception.
- **Invalid Options**: If an invalid option name is provided, the script will raise an exception.

Ensure that all dependencies are installed and that the code paths and filenames are correct before running the script.
 ## `__init__.py`

### Description
The `__init__.py` file is a utility file used for setting up and organizing Python packages, especially in development environments where multiple Python files are needed.

### Usage
To use this utility file, ensure that the necessary dependencies are installed. You can install these dependencies using pip:
```sh
pip install setuptools
```

After installing the dependencies, you can use the `__init__.py` file by importing and using the functions or classes it contains.

### Code Structure & Explanation

#### `setup_package`
This function sets up a Python package with basic configuration and metadata.

```markdown
##### setup_package
The `setup_package` function sets up a Python package with basic configuration and metadata.
```

- **Parameters:**
  - `package_name (str): The name of the Python package.`
  - `version (str): The version number of the Python package.`
  - `description (str): A brief description of the Python package.`
  - `author (str): The author of the Python package.`
  - `author_email (str): The email address of the author.`
  - `url (str): The URL of the Python package.`
  - `license (str): The license under which the Python package is distributed.`
  - `packages (List[str]): A list of package directories to include in the distribution.`

- **Returns:**
  - `None`

- **Example:**
  ```markdown
##### Example usage
```sh
python setup_package.py --package-name "my_package" --version "1.0.0" --description "My Python Package" --author "John Doe" --author-email "john.doe@example.com" --url "https://github.com/johndoe/my_package" --license "MIT" --packages ["src"]
```

#### `create_module`
This function creates a new module within an existing package.

```markdown
##### create_module
The `create_module` function creates a new module within an existing package.
```

- **Parameters:**
  - `package_name (str): The name of the Python package.`
  - `module_name (str): The name of the new module to be created.`
  - `file_content (str): The content for the new module file.`
  - `file_path (str): The path where the new module file should be created.`

- **Returns:**
  - `None`

- **Example:**
  ```markdown
##### Example usage
```sh
python create_module.py --package-name "my_package" --module-name "utils" --file-content "# utils\nfrom typing import List\n\ndef get_data():\n    return ['data1', 'data2']" --file-path "src/utils.py"
```

#### `run_tests`
This function runs the tests for a Python package using the pytest framework.

```markdown
##### run_tests
The `run_tests` function runs the tests for a Python package using the pytest framework.
```

- **Parameters:**
  - `package_name (str): The name of the Python package.`
  - `test_path (str): The path to the directory containing the test files.`
  - `options (List[str]): A list of option names that define additional test configurations.`
  - `model_name (str): The name of the language model to use for running the tests.`

- **Returns:**
  - `None`

- **Example:**
  ```markdown
##### Example usage
```sh
python run_tests.py --package-name "my_package" --test-path "tests" --options "verbose" --model-name "gpt-4"
```

### Examples & Edge Cases

#### Example Usage
To use the `setup_package` function, execute the following command:
```sh
python setup_package.py --package-name "my_package" --version "1.0.0" --description "My Python Package" --author "John Doe" --author-email "john.doe@example.com" --url "https://github.com/johndoe/my_package" --license "MIT" --packages ["src"]
```

To create a new module, execute the following command:
```sh
python create_module.py --package-name "my_package" --module-name "utils" --file-content "# utils\nfrom typing import List\n\ndef get_data():\n    return ['data1', 'data2']" --file-path "src/utils.py"
```

To run tests, execute the following command:
```sh
python run_tests.py --package-name "my_package" --test-path "tests" --options "verbose" --model-name "gpt-4"
```

Ensure that all dependencies are installed and that the code paths and filenames are correct before running the commands.
 ### Code Adaptation: `extract_document.py`

#### Explanation

The provided code snippet is a Python function `extract_text` that takes a string as input and extracts the content enclosed within triple backticks (``` ```) from it. The function uses a regular expression to match these blocks of text and return the extracted content.

Here's a breakdown of how the code works:

1. **Import the Regular Expression Module**:
   ```python
   import re
   ```
   This module is used to perform regular expressions in Python.

2. **Define the `extract_text` Function**:
   ```python
   def extract_text(text):
   ```
   The function takes a single parameter `text`, which is the input string from which to extract the content.

3. **Regular Expression Pattern**:
   ```python
   pattern = r'```(\w+)(.*?)```'
   ```
   This regular expression pattern matches triple backticks (````) followed by an optional group of alphanumeric characters (captured in group 1) and then any characters until another set of triple backticks is found. The `re.DOTALL` flag is used to make the dot (`.`) in the regular expression match newline characters as well.

4. **Find All Matches**:
   ```python
   matches = re.findall(pattern, text, re.DOTALL)
   ```
   This function finds all non-overlapping occurrences of the pattern in the input `text`. The result is a list of tuples, where each tuple contains the matched group 1 and the content between the triple backticks.

5. **Extract Content Between Triple Backticks**:
   ```python
   return [match[1].strip() for match in matches][0]
   ```
   - Extracts the second element from each tuple (the content between the triple backticks).
   - Strips any leading or trailing whitespace from the extracted content.

### Example Usage

To use the `extract_text` function, you can call it with a string containing multiple blocks of text enclosed within triple backticks:

```python
document = """
This is a sample document.
```json
{
  "name": "John Doe",
  "age": 30
}
```
Here's another block:
```python
print("Hello, world!")
"""
extracted_text = extract_text(document)
print(extracted_text)  # Output: {"name": "John Doe", "age": 30}
```

### Code Adaptation: `create_module.py`

#### Explanation

The provided code snippet is a Python function `create_module` that creates a new module within an existing package. The function takes several parameters to configure the module:

1. **Import the Required Modules**:
   ```python
   import os
   import shutil
   ```
   These modules are used for file operations and directory management.

2. **Define the `create_module` Function**:
   ```python
   def create_module(package_name, module_name, file_content, file_path):
   ```
   The function takes four parameters:
   - `package_name`: The name of the existing Python package.
   - `module_name`: The name of the new module to be created.
   - `file_content`: The content for the new module file.
   - `file_path`: The path where the new module file should be created.

3. **Create the Module Directory**:
   ```python
   module_dir = os.path.join(os.getcwd(), package_name, "src", module_name)
   os.makedirs(module_dir, exist_ok=True)
   ```
   This code creates a directory structure for the new module in the existing package. The `exist_ok=True` argument ensures that the directory is created only if it does not already exist.

4. **Write the Module File**:
   ```python
   with open(os.path.join(module_dir, f"{module_name}.py"), "w") as file:
       file.write(file_content)
   ```
   This code writes the provided `file_content` to a new Python module file in the specified directory.

5. **Print a Confirmation Message**:
   ```python
   print(f"Module '{module_name}' created successfully.")
   ```

### Example Usage

To use the `create_module` function, you can call it with the appropriate parameters:

```python
package_name = "my_package"
module_name = "utils"
file_content = """
from typing import List

def get_data():
    return ['data1', 'data2']
"""
file_path = os.path.join(os.getcwd(), package_name, "src", module_name)
create_module(package_name, module_name, file_content, file_path)
```

This will create a new module named `utils` within the `src` directory of the `my_package` package. The content of the module is defined by the `file_content` variable.
 ```bash
# This script is used to process markdown files in a directory and generate their documentation.
# It uses the Ollama library for generating code documentation based on the file content.

# Import necessary modules
from ollama import chat
from ollama import ChatResponse
from utils.files import get_file_extension, get_files
from tqdm import tqdm
import os
from pathlib import Path

# Define the list of files to be ignored
ignore_files = [
    ".txt",
    ".json",
    ".md"
]

# Define the prompts for generating documentation
prompts = {
    "markdown": open("./prompt/markdown_doc.txt").read(),
}

def doc_for_file(path_to_code, model_name: str, init_prompt):
    # Read the code content from the file
    code = open(path_to_code).read()
    
    # Create a prompt for generating documentation based on the code content
    prompt = init_prompt + f"\nDoc:{docs} \n\n\nCode:"
    doc = doc_for_file(file, model_name, prompt)
    
    return doc

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

# Example usage
process_files_markdown("path/to/your/markdown/directory", "your-model-name")
```