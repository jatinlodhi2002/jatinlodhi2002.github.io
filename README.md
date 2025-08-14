# DevOps & Cloud Engineer Portfolio

This directory contains a complete portfolio solution that converts Markdown to a professional HTML website with automatic GitHub Pages deployment.

## 📁 File Structure

```
portfolio/
├── devops-portfolio.md              # Your portfolio content (Markdown)
├── index.html                       # Main HTML template
├── style.css                        # Professional CSS styling
├── script.js                        # Interactive JavaScript
├── convert-markdown.py              # Markdown to HTML converter
├── github-pages-setup-guide.md     # Basic GitHub Pages setup
├── markdown-to-github-pages-guide.md # Complete automation guide
├── .github/
│   └── workflows/
│       └── deploy.yml               # Auto-deployment workflow
└── README.md                        # This file
```

## 🚀 Quick Start

### Option 1: Manual Conversion (Test Locally)
```bash
# Convert markdown to HTML
python convert-markdown.py devops-portfolio.md

# Open index.html in browser to preview
```

### Option 2: Auto-Deployment to GitHub Pages
1. Create repository named `your-username.github.io`
2. Upload all files from this directory
3. Enable GitHub Actions in repository settings
4. Your site will be live at `https://your-username.github.io`

## 📝 How to Update Your Portfolio

### For Auto-Deployment Setup:
1. Edit `devops-portfolio.md` with your content
2. Push changes to GitHub
3. Site automatically updates in 2-3 minutes

### For Manual Setup:
1. Edit `devops-portfolio.md`
2. Run `python convert-markdown.py devops-portfolio.md`
3. Upload updated `index.html` to your hosting

## 🎯 Features

- **Responsive Design** - Works on all devices
- **Professional Layout** - Modern, clean appearance
- **Automatic Conversion** - Markdown to HTML
- **Auto-Deployment** - Updates site when you push changes
- **SEO Optimized** - Proper meta tags and structure
- **Interactive Elements** - Smooth scrolling, animations

## 📖 Documentation

- `github-pages-setup-guide.md` - Basic GitHub Pages hosting
- `markdown-to-github-pages-guide.md` - Complete automation setup

## 🛠️ Customization

### To customize the design:
- Edit `style.css` for colors, fonts, layout
- Modify `index.html` for structure changes
- Update `script.js` for interactive features

### To modify content structure:
- Edit `convert-markdown.py` to change parsing logic
- Update section headers in your markdown file
- Adjust HTML template sections as needed

## 🔧 Requirements

- Python 3.6+ (for conversion script)
- Git (for GitHub deployment)
- GitHub account (for hosting)

## 📞 Support

If you need help:
1. Check the detailed guides in this directory
2. Ensure your markdown follows the expected format
3. Test conversion locally before deploying

---

**Your professional portfolio is ready to deploy! 🎉**
