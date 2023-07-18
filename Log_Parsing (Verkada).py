# Parse the logs in sample.log file and output the logs in csv format
# 
# INPUT FILE "sample.log" = 
# timestamp="19/Dec/2020:13:57:26 +0100" message="message_1" id=0 field_0="test message 0" field_1="test message 1"
# timestamp="19/Dec/2020:13:58:02 +0100" message="message_0" id=6 field_6="test message 2"
# timestamp="19/Dec/2020:13:58:16 +0100" message="message_2" id=3 field_16="test message 3" field_0="test message 4"
# timestamp="19/Dec/2020:13:58:28 +0100" message="message_5" id=8 field_8="test message 5"
# timestamp="19/Dec/2020:13:58:36 +0100" message="message_1" id=1 field_0="test message 6"
# timestamp="19/Dec/2020:13:58:58 +0100" message="message_3" id=5 field_1="test message 7"
# 
# 
# the output needs to be sorted by id field.
# missing fields should be outputted as empty values.
# the code needs to be able to parse all kinds of fields, not only limited to the ones in log sample
# if there are spaces in logs, the spaces would be wrapped in quotes
# values can be treated as strings, except the id fields used for sorting
# columns can be in any order
# apart from those parsing logs directly, any other libraries are allowed to use
# Google, Stackoverflow, or anything else needed are allowed to use for searching libraries or APIs, but are not allowed to use for searching "how to parse logs"
# 
# Example output
# 
# id,timestamp,message,field_0,field_1,field_6,field_16,field_8
# 0,"19/Dec/2020:13:57:26 +0100","message_1","test message 0","test message 1",,,
# 1,"19/Dec/2020:13:58:36 +0100","message_1","test message 6",,,,
# 3,"19/Dec/2020:13:58:16 +0100","message_2","test message 4",,,"test message 3",
# 5,"19/Dec/2020:13:58:58 +0100","message_3",,"test message 7",,,
# 6,"19/Dec/2020:13:58:02 +0100","message_0",,,"test message 2",,
# 8,"19/Dec/2020:13:58:28 +0100","message_5"
# 


