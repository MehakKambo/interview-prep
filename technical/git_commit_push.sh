#!/bin/bash

# This script is used to commit and push changes to the git repository
# Check if a commit message was passed as an argument

if [ -z "$1" ]; then
    echo "Error: No commit message provided!"
    echo "Usage: $0 <commit message>"
    exit 1
fi

# Add all changes to the git repository
git add .

# Commit the changes
git commit -m "$1"

# Push the changes to the remote repository
git push

echo "Changes committed and pushed to the remote repository."