# GitHub Pages Portfolio Hosting Guide

## 📋 Prerequisites
- GitHub account (create one at github.com if you don't have it)
- Git installed on Windows (download from git-scm.com)
- Your portfolio files ready (HTML, CSS, JS)

---

## 🚀 Step 1: Create GitHub Repository

### On GitHub Website:
• Log into your GitHub account
• Click the **"+"** icon in the top right corner
• Select **"New repository"**
• Repository name: `your-username.github.io` (replace with your actual GitHub username)
  - Example: If your username is "johnsmith", name it `johnsmith.github.io`
• Make sure it's set to **Public**
• Check **"Add a README file"**
• Click **"Create repository"**

**Important:** The repository name MUST be `your-username.github.io` for the main portfolio site.

---

## 💻 Step 2: Clone Repository to Your Computer

### Open Command Prompt or Git Bash:
• Press `Windows + R`, type `cmd`, press Enter
• Navigate to where you want to store your project:
```bash
cd C:\Users\YourName\Documents
```

• Clone your repository:
```bash
git clone https://github.com/your-username/your-username.github.io.git
```
Example:
```bash
git clone https://github.com/johnsmith/johnsmith.github.io.git
```

• Navigate into the repository folder:
```bash
cd your-username.github.io
```

---

## 📁 Step 3: Add Your Portfolio Files

### Copy Your Files:
• Open File Explorer and navigate to your cloned repository folder
• Copy all your portfolio files into this folder:
  - `index.html` (this MUST be your main page)
  - `style.css` or `styles.css`
  - `script.js` or any JavaScript files
  - `images/` folder (if you have images)
  - Any other assets (fonts, icons, etc.)

### File Structure Example:
```
your-username.github.io/
├── index.html          (REQUIRED - main page)
├── style.css
├── script.js
├── images/
│   ├── profile.jpg
│   └── project1.png
├── projects/
│   └── project-details.html
└── README.md
```

---

## 🔄 Step 4: Push Files to GitHub

### In Command Prompt/Git Bash:
• Check what files are ready to be added:
```bash
git status
```

• Add all your files:
```bash
git add .
```

• Commit your files with a message:
```bash
git commit -m "Add portfolio website files"
```

• Push to GitHub:
```bash
git push origin main
```

**Note:** If you get an error about "main" vs "master", try:
```bash
git push origin master
```

---

## 🌐 Step 5: Enable GitHub Pages

### On GitHub Website:
• Go to your repository on GitHub
• Click on **"Settings"** tab (at the top of the repository)
• Scroll down to **"Pages"** in the left sidebar
• Under **"Source"**, select **"Deploy from a branch"**
• Choose **"main"** branch (or "master" if that's what you have)
• Select **"/ (root)"** folder
• Click **"Save"**

### Wait for Deployment:
• GitHub will show a message: "Your site is ready to be published"
• It may take 5-10 minutes for the site to go live
• Refresh the Settings page to see the live URL

---

## 🔗 Step 6: Get Your Live URL

### Your Portfolio URL:
• Your live website will be available at:
```
https://your-username.github.io
```
Example: `https://johnsmith.github.io`

### Check if It's Live:
• Go to the URL in your browser
• If you see a 404 error, wait a few more minutes and refresh
• Make sure your main file is named `index.html`

---

## 🔄 Step 7: Update Your Site in the Future

### To Make Changes:
• Edit your files locally on your computer
• In Command Prompt/Git Bash, navigate to your repository folder:
```bash
cd C:\Users\YourName\Documents\your-username.github.io
```

• Add the changes:
```bash
git add .
```

• Commit with a descriptive message:
```bash
git commit -m "Update portfolio with new project"
```

• Push to GitHub:
```bash
git push origin main
```

• Changes will appear on your live site within 5-10 minutes

---

## 🛠️ Troubleshooting Tips

### Common Issues:

**Site shows 404 error:**
• Make sure your main file is named `index.html` (not `home.html` or anything else)
• Check that GitHub Pages is enabled in repository settings
• Wait 10-15 minutes after enabling GitHub Pages

**Git commands not working:**
• Make sure Git is installed: `git --version`
• Check you're in the correct folder: `pwd` (shows current directory)
• Verify remote connection: `git remote -v`

**Images not loading:**
• Use relative paths: `./images/photo.jpg` instead of `C:\Users\...`
• Check file names match exactly (case-sensitive)
• Make sure images are pushed to GitHub

**CSS/JS not loading:**
• Use relative paths: `./style.css` instead of absolute paths
• Check file names in your HTML match the actual file names
• Clear browser cache (Ctrl + F5)

---

## 📝 Quick Command Reference

### Essential Git Commands:
```bash
# Check status of files
git status

# Add all files
git add .

# Add specific file
git add filename.html

# Commit changes
git commit -m "Your message here"

# Push to GitHub
git push origin main

# Pull latest changes
git pull origin main

# Check current directory
pwd

# Change directory
cd folder-name

# Go back one directory
cd ..
```

---

## 🎯 Pro Tips

### For Better Portfolio Management:
• Create a `dev` branch for testing changes before going live
• Use meaningful commit messages like "Add new project section" instead of "update"
• Keep a backup of your files locally
• Test your site locally before pushing (use Live Server extension in VS Code)
• Optimize images for web to improve loading speed

### Custom Domain (Optional):
• You can use a custom domain like `yourname.com` instead of `username.github.io`
• Add a `CNAME` file with your domain name
• Configure DNS settings with your domain provider
• GitHub Pages supports HTTPS for custom domains

---

## ✅ Final Checklist

Before going live, make sure:
• [ ] Repository name is `your-username.github.io`
• [ ] Main file is named `index.html`
• [ ] All file paths use forward slashes `/` not backslashes `\`
• [ ] Images and assets are included in the repository
• [ ] GitHub Pages is enabled in repository settings
• [ ] Site loads correctly at your GitHub Pages URL

**Your portfolio will be live at:** `https://your-username.github.io`

---

*🎉 Congratulations! Your portfolio is now live and accessible to anyone on the internet. Share your URL with potential employers and on your social media profiles.*
