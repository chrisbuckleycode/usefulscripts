#!/usr/bin/env bash

# This script will convert a repo's mainline branch
# from "master" to "main"
# n.b. depending on your scm tool there may be
# alternative methods to achieve the same result.

MAINLINE_OLD="master"
MAINLINE_NEW="main"


BRANCH_EXISTS=$(git show-ref refs/heads/"$MAINLINE_OLD")
if [ -z "$BRANCH_EXISTS" ]; then                 # Check branch exists
    echo "No branch found with name $MAINLINE_OLD"
    exit 1
fi


echo "Renaming branch $MAINLINE_OLD to $MAINLINE_NEW"
git branch -m "$MAINLINE_OLD" "$MAINLINE_NEW"    # Rename the local branch
git push origin --set-upstream "$MAINLINE_NEW"   # Push the renamed local branch and set the upstream


if [ $? -eq 0 ]; then                            # Check if push was successful
    echo "Push successful."
    echo "Please go to the repo's settings and switch Default branch to the new name then"
    read -rp "Press Enter to continue..."
    echo " Deleting the old remote branch: $MAINLINE_OLD"
    git push origin --delete "$MAINLINE_OLD"     # Delete the old remote branch
else
    echo "Push failed. Aborting script."
    exit 1
fi

echo "Cleaning up local"
git fetch origin                                 # Fetch the latest changes from the remote repository
git remote prune origin                          # Remove any references to remote branches that no longer exist

git remote set-head origin -a                    # Restoring origin/HEAD

echo "List of new remote branches:"
git branch -r

echo "List of new local branches:"
git branch

