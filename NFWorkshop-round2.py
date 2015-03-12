import sys
import os
import re
import base64

# Directory containing tcpflow output files (include trailing backslash)
directory = sys.argv[1]

output_file = sys.argv[2]

outputdata = []

for filename in os.listdir(directory):

    with open(str(directory + filename), 'r') as flow:

        for line in flow.readlines():
                if re.search('PRIVMSG', line):
                    parsed_line = line.split(':')
                    strip_line = parsed_line[-1].strip()

                    try:
                        outputdata.append(str(line + '+++ Decoded ascii hex inside base64: ' +
                                              str(base64.b64decode(strip_line).decode('hex')) + '\n'))
                        continue
                    except:
                        pass
                    try:
                        outputdata.append(str(line + '+++ Decoded base32 inside base64: ' +
                                              str(base64.b32decode(base64.b64decode(strip_line))) + '\n'))
                        continue
                    except:
                        pass
                    try:
                        outputdata.append(str(line + '+++ Decoded double base64: ' +
                                              str(base64.b64decode(base64.b64decode(strip_line))) + '\n'))
                        continue
                    except:
                        pass
                    try:
                        outputdata.append(str(line + '+++ Decoded base64: ' +
                                              str(base64.b64decode(strip_line)) + '\n'))
                        continue
                    except:
                        pass
                else:
                    outputdata.append(str(line))

with open(output_file, 'wb+') as f:
    for line in outputdata:
        f.write(line)