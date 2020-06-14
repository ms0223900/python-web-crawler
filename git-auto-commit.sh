#!/bin/bash
read -p "Commit message: " commitMessage
git add -A
git commit -m "$commitMessage"
git push
