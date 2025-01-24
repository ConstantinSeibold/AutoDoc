import subprocess
import os

def change_to_git_repo(directory): 
    if os.path.isdir(os.path.join(directory, '.git')):
        try:
            os.chdir(directory)
            print(f"Successfully changed to the Git repository at {directory}")
        except FileNotFoundError:
            print(f"Directory not found: {directory}")
    else:
        print(f"{directory} is not a Git repository.")

def is_git_repo(directory):
    return os.path.isdir(os.path.join(directory, '.git'))

def get_changed_files():
    """
    Retrieve a list of files that have been changed since the last Git commit.
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

def get_untracked_files():
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

def get_added_files():
    """
    Retrieve a list of files that have been created/added since the last Git commit.
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

def get_files():
    files = get_changed_files()+get_added_files()+get_untracked_files()
    files = list(set(files))
    return files

def stage_all_changed_files():
    """
    Stages all changed files (including modified, added, and deleted files) for commit.
    """
    try:
        subprocess.run(['git', 'add', '--all'], check=True)
        print("All changed files have been staged.")
    except subprocess.CalledProcessError as e:
        print(f"Error staging files: {e}")

def commit_changes(commit_message):
    """
    Commits the staged changes with the given commit message.

    Parameters:
        commit_message (str): The commit message to use.
    """
    try:
        subprocess.run(['git', 'commit', '-m', commit_message], check=True)
        print(f"Changes have been committed with message: '{commit_message}'")
    except subprocess.CalledProcessError as e:
        print(f"Error committing changes: {e}")

# Example usage
if __name__ == "__main__":
    changed_files = get_changed_files()
    added_files = get_added_files()

    print("Changed Files:", changed_files)
    print("Added Files:", added_files)