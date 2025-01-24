import subprocess
import os

def change_to_git_repo(directory: str) -> None:
    """
    Change the current working directory to a Git repository.
    
    Parameters:
        directory (str): The path to the directory to change to.
        
    Returns:
        None
        
    Example:
        change_to_git_repo('/path/to/repo')
    """
    if os.path.isdir(os.path.join(directory, '.git')):
        try:
            os.chdir(directory)
            print(f"Successfully changed to the Git repository at {directory}")
        except FileNotFoundError:
            print(f"Directory not found: {directory}")
    else:
        print(f"{directory} is not a Git repository.")

def is_git_repo(directory: str) -> bool:
    """
    Check if a directory is a Git repository.
    
    Parameters:
        directory (str): The path to the directory to check.
        
    Returns:
        bool: True if the directory is a Git repository, False otherwise.
    """
    return os.path.isdir(os.path.join(directory, '.git'))

def get_changed_files() -> list[str]:
    """
    Retrieve a list of files that have been changed since the last Git commit.
    
    Parameters:
        None
        
    Returns:
        list[str]: A list of file paths that have been changed.
        
    Example:
        changed_files = get_changed_files()
        for file in changed_files:
            print(file)
    """
    try:
        result = subprocess.run(
            ['git', 'diff', '--name-only', '--diff-filter=M'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip().split('\n') if result.stdout else []
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving changed files: {e}")
        return []

def get_untracked_files() -> list[str]:
    """
    Retrieve a list of untracked files in the Git repository.
    
    Parameters:
        None
        
    Returns:
        list[str]: A list of file paths that are not tracked by Git.
        
    Example:
        untracked_files = get_untracked_files()
        for file in untracked_files:
            print(file)
    """
    try:
        # Run the 'git ls-files -o --exclude-standard' command to get untracked files
        result = subprocess.run(
            ['git', 'ls-files', '-o', '--exclude-standard'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            check=True
        )
        
        # Get the output of the command
        untracked_files = result.stdout.strip().split('\n')
        
        # If there are no untracked files, return an empty list
        if untracked_files == ['']:
            return []
        
        return untracked_files
    
    except subprocess.CalledProcessError as e:
        print(f"Error while fetching untracked files: {e.stderr}")
        return []

def get_added_files() -> list[str]:
    """
    Retrieve a list of new files that have been added since the last Git commit.
    
    Parameters:
        None
        
    Returns:
        list[str]: A list of file paths that have been added to the repository.
        
    Example:
        added_files = get_added_files()
        for file in added_files:
            print(file)
    """
    try:
        result = subprocess.run(
            ['git', 'diff', '--name-only', '--diff-filter=A'],
            capture_output=True,
            text=True,
            check=True
        )
        return result.stdout.strip().split('\n') if result.stdout else []
    except subprocess.CalledProcessError as e:
        print(f"Error retrieving added files: {e}")
        return []

def get_files() -> list[str]:
    """
    Retrieve a list of all files in the Git repository, including changed, added, and untracked files.
    
    Parameters:
        None
        
    Returns:
        list[str]: A list of file paths representing all files in the repository.
        
    Example:
        files = get_files()
        for file in files:
            print(file)
    """
    files = get_changed_files()+get_added_files()+get_untracked_files()
    files = list(set(files))
    return files

def stage_all_changed_files():
    """
    Stage all changed files (including modified, added, and deleted files) for commit.
    
    Parameters:
        None
        
    Returns:
        None
        
    Example:
        stage_all_changed_files()
    """
    try:
        subprocess.run(['git', 'add', '--all'], check=True)
        print("All changed files have been staged.")
    except subprocess.CalledProcessError as e:
        print(f"Error staging files: {e}")

def commit_changes(commit_message: str):
    """
    Commit the staged changes with the given commit message.
    
    Parameters:
        commit_message (str): The commit message to use.
        
    Returns:
        None
        
    Example:
        commit_changes('Initial commit')
    """
    try:
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        print(f"Changes committed with message: {commit_message}")
    except subprocess.CalledProcessError as e:
        print(f"Error committing changes: {e}")