import argparse
import re
import os

from actions import FlagAction

def get_filepath(args):
    matchstr = '.*-(?P<type>(?:release)|(?:debug))\.apk'
    if args.library:
        matchstr = 'classes\.jar'

    matches = list()
    if os.path.exists('bin/'):
        for f in os.listdir('bin/'):
            if re.match(matchstr, f):
                matches.append(re.match(matchstr, f))


    i = -1
    if len(matches) == 0:
        if args.library:
            print 'No classes.jar was found. Please verify this is an Android Library Project or remove the --library flag'
        else:
            print 'No apks were found. Please make sure this is a buildable android project or use the --library flag'
        quit()
    elif len(matches) > 1:
        print 'Which would you like to send:\n0) %s\n1) %s' % (matches[0].group(0), matches[1].group(0))
        while i != 0 and i != 1:
            try:
                i = input("Enter your selection: ")
            except:
                i = -1
    else:
        i = 0

    return 'bin/' + matches[i].group(0)

def process(args, msg):
    deliverable = get_filepath(args)
    msg.append_html('<p> File: %s </p>' % deliverable)
    if args.android_name:
        msg.append_html('<p> New Name: %s </p>' % args.android_name)

    msg.append_file(deliverable, args.android_name)

    return msg

def setup_args(parser):
    parser.add_argument('-l', '--library', dest='library', action=FlagAction, help='Indicates that this delivery is a library jar file', nargs=0)
    parser.add_argument('--new-name', dest='android_name', help='What youd wish to rename this deliverable to.')

