# Welcome to the Text-to-Speech Reader Tool
# This script uses the reader file to convert text to speech.

# Ensure you have the required libraries installed:
# pip install gtts playsound
# some reader file need to library

# Choosse the reader tool file
tool = "gtts_reader.py"

# Put your text here
text = """
Hello, this is an example text.
You can change it
"""

# Some options that required by reader file
reader_options = {}

#localization
localization = {
    "filenotfound": f"File not found: {tool}",
    "toolstopped": "Tool stopped",
}


# Main Python code
import importlib.util, os, re

if os.path.exists(tool):
    spec = importlib.util.spec_from_file_location("my_reader", tool)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    reader_instance = module.Reader(reader_options)
else:
    print(localization['filenotfound'])
    exit(1)

try:
    for sentence in text.split('.'):
        sentence = sentence.strip()
        if sentence:
            print(sentence+".", end="", flush=True)
            reader_instance.read(data=sentence)
            input()


except KeyboardInterrupt:
    print(f"\n*{localization['toolstopped']}*")
    reader_instance.exceptions_handle()