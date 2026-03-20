# 🤝 Contributing Guide

Thanks for contributing! Please follow this workflow to keep things clean and consistent.

## 🌿 Branching

Never commit directly to `main`. Always create a new branch for your work.

```bash
# Make sure you're on main and up to date
git checkout main
git pull origin main

# Create a new branch
git checkout -b feature/your-feature-name
```

**Branch naming conventions:**
- `feature/` — for new features (e.g. `feature/login-page`)
- `fix/` — for bug fixes (e.g. `fix/broken-navbar`)
- `docs/` — for documentation changes (e.g. `docs/update-readme`)

## ✏️ Making Changes

Make your changes, then stage and commit them:

```bash
# Stage your changes
git add .

# Commit with a clear message
git commit -m "Add login page with form validation"
```

**Good commit messages:**
- ✅ `Add user authentication flow`
- ✅ `Fix broken link in navbar`

**Bad commit messages:**
- ❌ `fixed stuff`
- ❌ `changes`

## 📤 Pushing & Opening a Pull Request

```bash
# Push your branch
git push origin feature/your-feature-name
```

Then go to the repo on GitHub and click **"Compare & pull request"**.

- Give your PR a clear title
- Fill out the pull request template
- Request a review from a teammate
- Wait for approval before merging

## 🐛 Reporting Issues

Use the **Issues** tab to report bugs or suggest features. Please use the provided templates so we have all the info we need.

## ❓ Questions

If you're stuck, leave a comment on the relevant issue or PR and a teammate will help you out.
