| Command                                    | Description                                                                       |
|--------------------------------------------|-----------------------------------------------------------------------------------|
| `git diff`                                 | Show unstaged file differences.                                                  |
| `git commit -a -m "commit message"`        | Commit all tracked changes with a message.                                       |
| `git status`                               | Show the state of your working directory.                                        |
| `git add file_path`                        | Add file(s) to the staging area.                                                 |
| `git checkout -b branch_name`              | Create and switch to a new branch.                                               |
| `git checkout branch_name`                 | Switch to an existing branch.                                                    |
| `git commit --amend`                       | Modify the last commit.                                                          |
| `git push origin branch_name`              | Push a branch to a remote repository.                                            |
| `git pull`                                 | Fetch and merge changes from a remote repository.                                |
| `git rebase -i`                            | Rebase interactively to rewrite commit history.                                  |
| `git clone`                                | Create a local copy of a remote repository.                                      |
| `git merge`                                | Merge branches together.                                                         |
| `git log --stat`                           | Show commit logs with stats.                                                     |
| `git stash`                                | Stash current changes for later.                                                 |
| `git stash pop`                            | Apply and remove stashed changes.                                                |
| `git show commit_id`                       | Show details about a specific commit.                                            |
| `git reset HEAD~1`                         | Undo the last commit but keep changes in working directory.                      |
| `git format-patch -1 commit_id`            | Create a patch file for a specific commit.                                       |
| `git apply patch_file_name`                | Apply changes from a patch file.                                                 |
| `git branch -D branch_name`                | Delete a branch forcefully.                                                      |
| `git reset`                                | Move branch pointer to a previous commit (preserve or discard changes).          |
| `git revert commit_id`                     | Undo a commit by creating a new commit that reverses it.                         |
| `git cherry-pick commit_id`                | Apply changes from a specific commit to the current branch.                      |
| `git branch`                               | List all branches.                                                               |
| `git reset --hard commit_id`               | Reset everything to a previous commit, discarding all changes.                   |
| `git fetch`                                | Download commits, files, and refs from a remote repository without merging.      |
| `git rm file_path`                         | Remove files from the working directory and staging area.                        |
| `git config --global user.name "Your Name"`| Set the global Git username.                                                     |
| `git config --global user.email "Your Email"` | Set the global Git email.                                                      |
| `git log --oneline`                        | Show a simplified view of commit history.                                        |



The sequence to merge a branch into the main branch is as follows:
```cmd
git checkout main
git pull origin main
git merge *branch_to_be_merged_into_main*
git push origin main
```