from .Main import Main

print(
    f"Hi, I'll ask you from which source repo to which target repo you want to copy the issues, then I'll download browser controllers and ensure the firefox browser is installed. Next I will scrape the issues from the source repo, and add them as new issues to the target repo. You can simply see what I do in the browser. Terminate me with CTRL+C if you don't like it. I'll let you know when I'm done."
)
project_nr = 1

main = Main(project_nr)

print(f"Done.")
