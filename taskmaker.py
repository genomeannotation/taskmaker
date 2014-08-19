#!/usr/bin/env python

import sys

# We want this to work with all python versions
if sys.version_info[0] < 3:
    def input(prompt):
        return raw_input(prompt)

def main():
    # Defualts
    default_shell = "/bin/sh"
    default_queue = "all.q"

    # Read values
    name = input("Job name: ")
    
    shell = input("Shell (default is %s): " % default_shell)
    shell = shell or default_shell

    use_env = input("Use environment variables? (y/n): ")
    use_env = (use_env == "Y" or use_env == "y")

    use_cwd = input("Use current working directory? (y/n): ")
    use_cwd = (use_cwd == "Y" or use_cwd == "y")

    out = input("Job output file (default is %s): " % (name+"<job_id>.out"))
    out = out or name+"$JOB_ID.out"

    queue = input("What queue do you want it to run on? (default is %s): " % default_queue)
    queue = queue or default_queue

    command = input("What command do you want to run?: ")

    # Output script
    outfile = sys.stdout
    
    outfile.write("#!/bin/sh\n")
    outfile.write("#$-N %s\n" % name)
    outfile.write("#$-S %s\n" % shell)
    if use_env:
        outfile.write("#$-V\n")
    if use_cwd:
        outfile.write("#$-cwd\n")
    outfile.write("#$-o %s\n" % out)
    outfile.write("#$-q %s\n" % queue)
    outfile.write(command+"\n")

####################################

if __name__ == "__main__":
    main()
