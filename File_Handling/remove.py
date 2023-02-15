# import os
# os.remove("demofile3.txt")
import os
if os.path.exists("demofileee.txt"):
  os.remove("demofile.txt")
else:
  print("The file does not exist")