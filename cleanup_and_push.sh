#!/usr/bin/env bash
set -e

# 1) Create or overwrite .gitignore
cat > .gitignore <<'EOF'
# Node
frontend/node_modules/
frontend/dist/

# Python
api/.venv/
**/__pycache__/
**/*.py[cod]
**/*.dist-info/

# Vercel output
.vercel/

# Misc
*.log
.DS_Store
EOF

# 2) Remove any dependency/build folders from the Git index
git rm -r --cached frontend/node_modules frontend/dist api/.venv .vercel || true

# 3) Stage everything (Git will respect .gitignore now)
git add .

# 4) Commit
git commit -m "chore: clean up repo, add .gitignore"

# 5) Push (to origin/main—change if needed)
git push origin master

echo "✅ Repo cleaned and pushed to origin/main"
