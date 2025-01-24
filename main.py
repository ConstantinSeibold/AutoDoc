# Import necessary libraries
import argparse, os  # For command line argument parsing
from code_adaptation.changes import process_files  # For modifying code
from utils.git import get_files, is_git_repo, change_to_git_repo, stage_all_changed_files, commit_changes


def main():
    """
    Main function to handle the execution of the script.
    Sets up the argument parser and processes the provided arguments to interact with an AI model using Ollama's API.
    """

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Chat with an AI model using Ollama's API.")
    parser.add_argument('--model', type=str, default="qwen2.5-coder:1.5b", help="The model to use (e.g., 'llama3.2').")
    parser.add_argument('--path', type=str, required=True, help="A file path to check (for future functionality).")
    parser.add_argument('--message', type=str, required=False, help="The message to send to the AI model.")
    parser.add_argument('--tasks', type=str, nargs='+', choices=['all','comments', 'docstring', 'linting', 'typehinting'],
                        help="Select one or more tasks to perform: comments, docstring, linting.")

    # Parse arguments
    args = parser.parse_args()

    # Extract arguments
    model_name = args.model
    path = args.path
    user_message = args.message
    tasks = args.tasks
    
    # Display selected tasks
    if tasks:
        print("Selected tasks:", ", ".join(tasks))

    if is_git_repo(path):
        change_to_git_repo(path)
        files = get_files()
        
        # Linting: Apply proper linting to the code, ensuring it adheres to best practices and follows the specific language's conventions. Focus on:
        # Proper indentation and formatting.
        # Consistent use of variable names and avoiding shadowing.
        # Appropriate spacing around operators and control structures.
        # Removal of redundant code or unnecessary comments.
        # Optimal use of language-specific features.
        # Elimination of unused variables, functions, or imports.
        
        process_files(files, tasks, model_name)
        
        # Stage all changed files
        stage_all_changed_files()
        
        # Commit changes
        commit_changes(user_message + "(automatically documented)")
    else:
        print(f"{path} is not a git directory.")

if __name__ == "__main__":
    main()