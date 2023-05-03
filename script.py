from argparse import ArgumentParser

from pygit2 import init_repository, Patch
from colorama import Fore

def compare_and_print(repo_path, commit_a, commit_b):
    # Load the repository from disk
    git_repo = init_repository(repo_path)

    # Get the diff between the two supplied commits, can be multiple apart. 
    diff = git_repo.diff(commit_a, commit_b, context_lines=0, interhunk_lines=0)
    
    # A diff contains Patches or Diffs. We care about patches (changes in a file)
    for obj in diff:
        if type(obj) == Patch:
            # You could get multiple patches for a single file, these are not grouped. Do not really care for this POC.
            print(f"Found a patch for file {obj.delta.new_file.path}")
            
            # A hunk is the change in a file, plus some lines surounding the change. This allows merging etc. in Git. 
            # https://www.gnu.org/software/diffutils/manual/html_node/Hunks.html
            for hunk in obj.hunks:
              # loop over the changes in the patch
              for line in hunk.lines:
                # The new_lineno represents the new location of the line after the patch. If it's -1, the line has been deleted.
                if line.new_lineno == -1: 
                    print(f"[{Fore.RED}removal line {line.old_lineno}{Fore.RESET}] {line.content.strip()}")
                # Similarly, if a line did not previously have a place in the file, it's been added fresh. 
                if line.old_lineno == -1: 
                    print(f"[{Fore.GREEN}addition line {line.new_lineno}{Fore.RESET}] {line.content.strip()}")  
                # We do not currently care for lines that have moved new != old, or lines that stayed in the same position. 

if __name__ == "__main__":
    parser = ArgumentParser()
    # Just copy the example :P
    parser.add_argument("repo_path")
    parser.add_argument("commit_a")
    parser.add_argument("commit_b")

    args = parser.parse_args()

    compare_and_print(args.repo_path, args.commit_a, args.commit_b)

