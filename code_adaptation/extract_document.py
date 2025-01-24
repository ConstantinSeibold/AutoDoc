import re

def extract_text(text):
    # Regular expression pattern to find text between ```word and ```
    pattern = r'```(\w+)(.*?)```'
    matches = re.findall(pattern, text, re.DOTALL)
    
    # Extracting the second element in the tuple (which is the text between backticks)
    return [match[1].strip() for match in matches][0]
