from argparse import ArgumentParser

from pygit2 import init_repository, Patch
from colorama import Fore

def compare_and_print(repo_path, commit_a, commit_b):

    git_repo = init_repository(repo_path)
    diff = git_repo.diff(commit_a, commit_b, context_lines=0, interhunk_lines=0)
    
    for obj in diff:
        if type(obj) == Patch:
            print(f"Found a patch for file {obj.delta.new_file.path}")
            for hunk in obj.hunks:
              for line in hunk.lines:
                if line.new_lineno == -1: 
                    print(f"[{Fore.RED}removal line {line.old_lineno}{Fore.RESET}] {line.content.strip()}")
                if line.old_lineno == -1: 
                    print(f"[{Fore.GREEN}addition line {line.new_lineno}{Fore.RESET}] {line.content.strip()}")  

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("repo_path")
    parser.add_argument("commit_a")
    parser.add_argument("commit_b")

    args = parser.parse_args()

    compare_and_print(args.repo_path, args.commit_a, args.commit_b)

