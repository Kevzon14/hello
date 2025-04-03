import os
import subprocess
import tempfile


message = "hanime.tv"


temp_dir = tempfile.gettempdir()
gandalf_message_file = os.path.join(temp_dir, "gandalf_message.txt")

with open(gandalf_message_file, "w") as file:
    file.write(message)

subprocess.Popen(["Microsoft Edge.exe", gandalf_message_file])
