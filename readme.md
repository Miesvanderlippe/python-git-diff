# Python Git Diff

A simple script to get a Python Diff. An experiment using PyGit2. 

# Examples 
This line was changed.


```sh
python3 script.py ./.git 800cde4d7a6dbfea94c9e83e0e4d527d96a87e26 086688590be41370fb120afc3fbe9c5f05b119f9

Found a patch for file readme.md
[removal line 6] This is the original line.
[addition line 6] This line was changed.
``` 
