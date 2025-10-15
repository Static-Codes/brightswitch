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
