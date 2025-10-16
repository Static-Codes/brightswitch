# Quick Start Guide:
  ## Making a permanent link to the application
  <code>apt install nano -y && nano ~/.bash_aliases</code>
  - Add the following line
    - Replace the path with the location of your downloaded copy:
  <code>alias brightshift="python3 path/to/brightshift/main.py"</code>
  - Saving the file with nano:
    - Ctrl + X
    - y
    - Enter
  - Reloading aliases
    <code>source ~/.bash_aliases && source ~/.bashrc</code>

# Variables To Know:
#### x = Monitor Name (See brightswitch --help) 
#### y = Brightness (A float representing the desired brightness)

# Supported Commands
### Change the specified monitor to the specified brightness (0 < y <= 1)
<code>brightswitch --monitor==(x) --brightness==(y)</code>

### Change ALL monitors to the specified brightness (0 < y <= 1)
<code>brightswitch --all --brightness==(y)</code>

### Lists the port identifiers associated with each monitor (Recommended to get these directly from your distro's display manager)
<code>brightswitch --list</code>
