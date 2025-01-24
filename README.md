Automatic Documentation and Git Commit Tool

## Overview

This script is designed to automate the process of generating documentation for code, including adding comments, docstrings, and performing linting or type hinting improvements. It integrates with an AI model via the Ollama API and utilizes Git for version control. The tool automatically stages and commits changes to the Git repository after processing the code.

### Features

- **Automatic Documentation Generation**: It automatically generates and inserts comments, docstrings, and type hints into your code files.
- **AI-Powered Assistance**: The tool leverages an AI model (via Ollama) to enhance the code documentation process.
- **Git Integration**: It detects if the provided path is a Git repository, stages changes, and commits them automatically with relevant messages.
- **Customizable Tasks**: Users can specify tasks like comments, docstrings, linting, or type hinting, and the script will perform the selected actions.
  
This is a work-in-progress tool that continues to evolve for enhancing the development workflow.

## Requirements

Before running the script, ensure that you have the following dependencies installed:

- `tqdm` library (for command-line argument parsing)
- `ollama` (for interacting with the AI model)
  
## Usage

To run the script, use the following command:

```bash
python main.py --model <model_name> --path <repo_path> --tasks <task1> <task2> ...
```

### Arguments:

- `--model`: (Optional) The AI model to use for processing code (default: `qwen2.5-coder:1.5b`).
- `--path`: (Required) The path to the directory or repository to process.
- `--message`: (Optional) A custom message to send to the AI model.
- `--tasks`: (Optional) A list of tasks to perform on the code. Choose from:
  - `comments`: Add comments to the code.
  - `docstring`: Add or update docstrings in the code.
  - `linting`: Perform linting to clean up the code.
  - `typehinting`: Add or improve type hints in the code.
  - `all`: Perform all available tasks.

### Example:

```bash
python main.py --model "qwen2.5-coder:1.5b" --path "/path/to/your/repo" --tasks comments docstring
```

This will:
- Use the `qwen2.5-coder:1.5b` model.
- Process the files in the specified path (`/path/to/your/repo`).
- Add comments and docstrings to the code files.

## Git Workflow

- If the specified path is a Git repository:
  1. It checks if the repository contains changes that need to be staged.
  2. Automatically stages all modified files.
  3. Commits the changes with a message indicating the code was automatically documented.
  4. Optionally, commits changes again after the documentation updates.

- If the specified path is not a Git repository, an error message will be shown.

## Current Limitations

- The tool is still in development, so some features might not be fully implemented or may need improvements.
- It currently does not support specifying custom commit messages with detailed information for each file.

## Future Work

- Improve AI interaction for better documentation generation.
- Add support for more Git operations (e.g., branching).
- Enhance the flexibility of task execution (e.g., conditional tasks).
- Improve error handling and edge-case management.

## Contributing

Feel free to open issues or pull requests to improve the functionality or fix bugs.

## License

This project is licensed under the MIT License - see the LICENSE file for details.