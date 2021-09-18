from .Main import Main



# Parse arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument(
    "--hc",
    dest="use_hardcoded_source_and_target", # way to specify the target boolean value.
    action="store_true", # way to set the value of the destination variable to True.
    help="boolean flag, determines whether the the hardcoded source and target repositories are used or whether the user is prompted to supply these manually",
)
parser.set_defaults(
    use_hardcoded_source_and_target=False,
)
args = parser.parse_args()

print(f'args.use_hardcoded_source_and_target={args.use_hardcoded_source_and_target}')
if args.use_hardcoded_source_and_target:
    print(f"Hi, I'll log in and start copying issues from/to the hardcoded source and target. When it is done, I'll let you know.")
else:
    print(
        f"Hi, I'll ask you from which source repo to which target repo you want to copy the issues, then I'll download browser controllers and ensure the firefox browser is installed. Next I will scrape the issues from the source repo, and add them as new issues to the target repo. You can simply see what I do in the browser. Terminate me with CTRL+C if you don't like it. I'll let you know when I'm done."
    )


# Initilialise object that controls execution of code.
project_nr = 1
main = Main(project_nr,args.use_hardcoded_source_and_target)

print(f"Done.")
