#!/usr/bin/env bash
set -e

echo "🧹 Starting cleanup process..."

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
*.egg-info/
.pytest_cache/
.coverage
htmlcov/

# Vercel output
.vercel/
.output/

# Misc
*.log
.DS_Store
EOF

# 2) Clean Python cache files
echo "🧹 Cleaning Python cache files..."
find . -type d -name "__pycache__" -exec rm -r {} +
find . -type f -name "*.pyc" -delete
find . -type f -name "*.pyo" -delete
find . -type f -name "*.pyd" -delete
find . -type d -name "*.egg-info" -exec rm -r {} +
find . -type d -name ".pytest_cache" -exec rm -r {} +

# 3) Remove any dependency/build folders from the Git index
echo "🧹 Removing cached build artifacts..."
git rm -r --cached frontend/node_modules frontend/dist api/.venv .vercel .output || true

# 4) Stage everything (Git will respect .gitignore now)
echo "📦 Staging changes..."
git add .

# 5) Commit
echo "💾 Committing changes..."
git commit -m "chore: clean up repo, add .gitignore"

# 6) Push (to origin/main—change if needed)
echo "🚀 Pushing to remote..."
git push origin master

echo "✅ Repo cleaned and pushed to origin/master"
