from git import *
from actions import FlagAction

def pretty_print_logs(since, until, graph):
    try:
        git = Git('./')
        r = ''
        if since:
            r = since
            if not until:
                until = 'HEAD'
        if until and r != '':
            r = r + '..' + until
        else:
            r = until

        if graph:
            g = '--graph'
        else:
            g = ''

        conv = Ansi2HTMLConverter()

        output = git.log(r, g, "--color", "--pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset'", "--abbrev-commit", "--")
        return conv.convert(output)
    except:
        print 'Error accessing git logs for this directory. Please verify that you are in a git repository.  Aborting delivery.'
        quit()

def tag_commit():
    try:
        pass
    except:
        print 'Error tagging in this directory. Please verify that you are in a git repository.  Aborting delivery.'
        quit()

def process(args, msg):
    if args.git_since or args.git_until:
        msg.append_html('<div>' + pretty_print_logs(args.git_since, args.git_until, args.git_graph) + '</div>')

    return msg

def setup_args(parser):
    parser.add_argument('--git-since', metavar='COMMIT_SINCE', dest='git_since', help='Attach the git log since a given commit')
    parser.add_argument('--git-until', metavar='COMMIT_UNTIL', dest='git_until', help='Attach the git log until a given commit')
    parser.add_argument('--git-graph', nargs=0, action=FlagAction, dest='git_graph', help='Turn on the graph output for git logs.  Git logs require either --git-since and/or --git-until')

