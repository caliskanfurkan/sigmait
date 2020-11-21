"title": "Creates files in the user directory",
"title": "Starts itself from another location",
"title": "Drops a file with a compile date too recent",
"title": "Writes to a start menu file",
"title": "Changes the autorun value in the registry",


Source: process -> process_create
	
      "u""count":1,
      "u""title":"u""Uses NETSH.EXE for network configuration",
      "u""process":"u""53fc4fdd-b1ef-42bf-8319-34186194aa43",
      "u""source":"u""process",
      "u""mitre":[
         "u""T1089"
      ],
      "u""threatLevel":1,
      "u""events":[
         {
            "u""cmdline":"u""netsh firewall add allowedprogram \"C:\\Users\\admin\\AppData\\Roaming\\Windows.exe\" \"Windows.exe\" ENABLE",
            "u""image":"u""C:\\Windows\\system32\\netsh.exe",
            "u""time":1605969741468
         }

Source: drops   -> filemod 
	
	{
      "u""count":1,
      "u""title":"u""Executable content was dropped or overwritten",
      "u""process":"u""53fc4fdd-b1ef-42bf-8319-34186194aa43",
      "u""source":"u""drops",
      "u""mitre":"None",
      "u""threatLevel":1,
      "u""events":[
         {
            "u""time":1605969741546,
            "u""md5":"u""800f2e4fbc4e28960afd2236887a93b6",
            "u""filename":"u""C:\\Users\\admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\f9a53957252f1763c1116f67c8274c9f.exe",
            "u""size":37888
         }

Source: registry -> regmod,  REG_SZ, operation:write


	 "u""events":[
         {
            "u""name":"u""f9a53957252f1763c1116f67c8274c9f",
            "u""typeValue":"u""REG_SZ",
            "u""value":"u""\"C:\\Users\\admin\\AppData\\Roaming\\Windows.exe\" ..",
            "u""key":"u""HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Run",
            "u""time":1605969741500,
            "u""operation":"u""write",
            "u""_id":"u""5fb9274e44f3ca15a176acfe"
         },
