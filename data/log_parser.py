import re

with open('rsvp_agent_log.dat', 'r') as log_file:
    print('WARNINGS:')
    for line in log_file.readlines():
        if re.search('WARNING', line):
            print(re.sub(r'WARNING:\S+:', '--', line))