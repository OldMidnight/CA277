#!/usr/bin/env python

import sys
import time
files = sys.argv[1:]

i = 0
# Set Tag Variables
li_start = '<li>'
li_end = '</li>' + '\n'
ul_start = '<ul>' + '\n'
ul_end = '</ul>' + '\n'
pre_start = '<pre>' + '\n'
pre_end = '</pre>' + '\n'
p_start = '<p>' + '\n'
p_end = '</p>' + '\n'

def check_for_bold(s):
    s = s.split()
    s_count = 0
    while s_count < len(s):
        word = s[s_count]
        if word[0] == '*':
            if word[-1] == '.' or word[-1] == ',':
                s[s_count] = '<b>' + word[1:-2] + '</b>' + word[-1]
            else:
                s[s_count] = '<b>' + word[1:-1] + '</b>'
        s_count += 1
    s = ' '.join(s) + '\n'
    return s

def check_for_italics(s):
    s = s.split()
    #print 'first pass:', s
    s_count = 0
    while s_count < len(s):
        word = s[s_count]
    #    print 'first pass:', word
        # check if first charachter is an underline on first pass
        if word[0] == '_':
            s[s_count] = '<i>' + word[1:]
        s_count += 1
    #print 'second pass:', s
    s_count = 0
    while s_count < len(s):
        word = s[s_count]
    #    print 'second pass:', word
        # make sure word isnt the last in the sentence, this is to make sure puntuayion isnt included in formatting.
        if word[-1] == '.' or word[-1] == ',':
            if word[-2] == '_':
                s[s_count] = word[:-2] + '</i>' + word[-1]
        else:
            if word[-1] == '_':
                s[s_count] = word[:-1] + '</i>'
        s_count += 1
    s = ' '.join(s) + '\n'
    #print s
    return s

# Loop to read and process all lines from all files
while i < len(files):
    in_file = files[i]
    out_file = in_file + '.html'
    with open(in_file) as f_in:
        lines = f_in.readlines()
    
    # Open Output file
    with open(out_file, 'w') as f_out:
        line_count = 0
        while line_count < len(lines):
            line = lines[line_count].rstrip()
        #    print line
            print len(line)
            if len(line) > 0:# Fix index error from block gaps
                if line[0] == ' ':
                    f_out.write(pre_start)
                    pre_count = line_count# Start counting from the current line
                    while pre_count < len(lines) and lines[pre_count][0] == ' ':
                        pre_count += 1
                    # List of all pre formatted lines
                    pre_list = lines[line_count:pre_count]
                    pre_list_count = 0
                    while pre_list_count < len(pre_list):
                        f_out.write(pre_list[pre_list_count].rstrip() + '\n')
                        pre_list_count += 1
                    f_out.write(pre_end)
                    # set current line to the last preformatted line
                    line_count = pre_count
                else:
                    if line[0] == '#':
                        k = 0
                        while k < len(line) and line[k] == '#':
                            k += 1
                        # what weight is the header
                        h_type = str(len(line[:k]))
                        k += 1
                        # text of the header
                        header = line[k:].strip()
                        f_out.write('<h' + h_type + '>' + header + '</h' + h_type + '>' + '\n')
                        line_count += 1
                    elif line[0] == '-':
                        # start counting from current line
                        f_out.write(ul_start)
                        list_count = line_count
                        # create list to place all list items
                        list_item_list = []
                        while list_count < len(lines) and lines[list_count][0] == '-':
                            list_item_list.append(lines[list_count][2:])
                            list_count += 1
                        list_item_list_count = 0
                        while list_item_list_count < len(list_item_list):
                            # write to file, but only after checking for bold and italics
                            f_out.write(li_start + check_for_italics(check_for_bold(list_item_list[list_item_list_count])).strip() + li_end)
                            list_item_list_count += 1
                        f_out.write(ul_end)
                        line_count = list_count
                    else:
                        # if it reaches here, it must be a <p> as all check for formatting failed
                        f_out.write(p_start)
                        p_count = line_count
                        # make sure the line you are counting is not a newline char otherwise newlines will appear in your html file
                        while p_count < len(lines) and lines[p_count] != '\n':
                            p_count += 1
                        # list of all lines in the <p> tag
                        p_list = lines[line_count:p_count]
                        p_list_count = 0
                        while p_list_count < len(p_list):
                            # only write to file after checking for bold and italic
                            f_out.write(check_for_italics(check_for_bold(p_list[p_list_count])))
                            p_list_count += 1
                        f_out.write(p_end)
                        line_count = p_count
            else:
                line_count += 1
    i += 1
