#!/usr/bin/env python3
"""
Markdown to HTML Portfolio Converter
Converts a markdown portfolio file to a professional HTML website
"""

import re
import os
import sys
from pathlib import Path

def read_file(filepath):
    """Read content from a file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as file:
            return file.read()
    except FileNotFoundError:
        print(f"Error: File '{filepath}' not found.")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

def write_file(filepath, content):
    """Write content to a file"""
    try:
        with open(filepath, 'w', encoding='utf-8') as file:
            file.write(content)
        print(f"✓ Created: {filepath}")
    except Exception as e:
        print(f"Error writing file: {e}")
        sys.exit(1)

def extract_sections(markdown_content):
    """Extract different sections from markdown content"""
    sections = {}
    
    # Extract About Me section
    about_match = re.search(r'## 🚀 About Me\s*\n(.*?)(?=\n## |\n---|\Z)', markdown_content, re.DOTALL)
    sections['about'] = about_match.group(1).strip() if about_match else ""
    
    # Extract Skills section
    skills_match = re.search(r'## 🛠️ Technical Skills\s*\n(.*?)(?=\n## |\n---|\Z)', markdown_content, re.DOTALL)
    sections['skills'] = skills_match.group(1).strip() if skills_match else ""
    
    # Extract Projects section
    projects_match = re.search(r'## 🎯 Featured Projects\s*\n(.*?)(?=\n## |\n---|\Z)', markdown_content, re.DOTALL)
    sections['projects'] = projects_match.group(1).strip() if projects_match else ""
    
    # Extract Experience section
    experience_match = re.search(r'## 💼 Professional Experience\s*\n(.*?)(?=\n## |\n---|\Z)', markdown_content, re.DOTALL)
    sections['experience'] = experience_match.group(1).strip() if experience_match else ""
    
    # Extract Contact section
    contact_match = re.search(r'## 📞 Contact & Professional Links\s*\n(.*?)(?=\n## |\n---|\Z)', markdown_content, re.DOTALL)
    sections['contact'] = contact_match.group(1).strip() if contact_match else ""
    
    return sections

def convert_markdown_to_html(text):
    """Convert basic markdown to HTML"""
    # Headers
    text = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', text, flags=re.MULTILINE)
    
    # Bold text
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    
    # Italic text
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    
    # Code blocks
    text = re.sub(r'```(.*?)```', r'<pre><code>\1</code></pre>', text, flags=re.DOTALL)
    
    # Inline code
    text = re.sub(r'`(.*?)`', r'<code>\1</code>', text)
    
    # Links
    text = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2" target="_blank">\1</a>', text)
    
    # Lists
    lines = text.split('\n')
    in_list = False
    result_lines = []
    
    for line in lines:
        if re.match(r'^[-•]\s+', line):
            if not in_list:
                result_lines.append('<ul>')
                in_list = True
            item_text = re.sub(r'^[-•]\s+', '', line)
            result_lines.append(f'<li>{item_text}</li>')
        else:
            if in_list:
                result_lines.append('</ul>')
                in_list = False
            result_lines.append(line)
    
    if in_list:
        result_lines.append('</ul>')
    
    # Paragraphs
    text = '\n'.join(result_lines)
    paragraphs = text.split('\n\n')
    html_paragraphs = []
    
    for para in paragraphs:
        para = para.strip()
        if para and not para.startswith('<'):
            html_paragraphs.append(f'<p>{para}</p>')
        elif para:
            html_paragraphs.append(para)
    
    return '\n'.join(html_paragraphs)

def parse_skills(skills_content):
    """Parse skills section into categories"""
    skills_html = ""
    current_category = ""
    current_skills = []
    
    lines = skills_content.split('\n')
    
    for line in lines:
        line = line.strip()
        if line.startswith('### '):
            # Save previous category
            if current_category and current_skills:
                icon = get_skill_icon(current_category)
                skills_html += f'''
                <div class="skill-category">
                    <h3><i class="{icon}"></i> {current_category}</h3>
                    <ul>
                        {''.join([f'<li>{skill}</li>' for skill in current_skills])}
                    </ul>
                </div>
                '''
            
            # Start new category
            current_category = line.replace('### ', '').replace('☁️ ', '').replace('🔄 ', '').replace('🏗️ ', '').replace('📦 ', '').replace('📊 ', '').replace('💻 ', '').replace('🔧 ', '')
            current_skills = []
        elif line.startswith('- **'):
            # Extract skill
            skill_match = re.search(r'- \*\*(.*?)\*\*(.*)', line)
            if skill_match:
                skill_name = skill_match.group(1)
                skill_desc = skill_match.group(2).strip(' -')
                current_skills.append(f'<strong>{skill_name}</strong>{skill_desc}')
    
    # Add last category
    if current_category and current_skills:
        icon = get_skill_icon(current_category)
        skills_html += f'''
        <div class="skill-category">
            <h3><i class="{icon}"></i> {current_category}</h3>
            <ul>
                {''.join([f'<li>{skill}</li>' for skill in current_skills])}
            </ul>
        </div>
        '''
    
    return skills_html

def get_skill_icon(category):
    """Get appropriate icon for skill category"""
    icons = {
        'Cloud Platforms': 'fas fa-cloud',
        'CI/CD Tools': 'fas fa-sync-alt',
        'Infrastructure as Code': 'fas fa-code',
        'Containers & Orchestration': 'fab fa-docker',
        'Monitoring & Logging': 'fas fa-chart-line',
        'Scripting Languages': 'fas fa-terminal',
        'Version Control & Collaboration': 'fab fa-git-alt'
    }
    return icons.get(category, 'fas fa-tools')

def parse_projects(projects_content):
    """Parse projects section into cards"""
    projects_html = ""
    
    # Split by project headers
    project_sections = re.split(r'### \d+\.\s*', projects_content)
    
    for section in project_sections[1:]:  # Skip first empty section
        if not section.strip():
            continue
            
        lines = section.strip().split('\n')
        title = lines[0].strip()
        
        # Extract project details
        description = ""
        technologies = []
        achievements = []
        
        current_section = ""
        for line in lines[1:]:
            line = line.strip()
            if line.startswith('**Description:**'):
                current_section = "description"
                description = line.replace('**Description:**', '').strip()
            elif line.startswith('**Technologies Used:**'):
                current_section = "tech"
            elif line.startswith('**Key Achievements:**'):
                current_section = "achievements"
            elif line.startswith('- ') and current_section == "tech":
                tech = line.replace('- ', '').replace('**', '').split(',')
                technologies.extend([t.strip() for t in tech])
            elif line.startswith('- ') and current_section == "achievements":
                achievements.append(line.replace('- ', ''))
            elif current_section == "description" and line:
                description += " " + line
        
        # Generate tech tags
        tech_tags = ''.join([f'<span class="tech-tag">{tech}</span>' for tech in technologies[:8]])  # Limit to 8 tags
        
        # Generate achievements list
        achievements_html = ''.join([f'<li>{achievement}</li>' for achievement in achievements[:4]])  # Limit to 4 achievements
        
        projects_html += f'''
        <div class="project-card">
            <div class="project-header">
                <h3>{title}</h3>
            </div>
            <div class="project-content">
                <p>{description}</p>
                <div class="project-tech">
                    {tech_tags}
                </div>
                <div class="project-achievements">
                    <h4>Key Achievements:</h4>
                    <ul>
                        {achievements_html}
                    </ul>
                </div>
            </div>
        </div>
        '''
    
    return projects_html

def parse_experience(experience_content):
    """Parse experience section into timeline"""
    experience_html = ""
    
    # Split by job titles (assuming they start with ###)
    job_sections = re.split(r'### (.*?) \| (.*?) \| (.*?)$', experience_content, flags=re.MULTILINE)
    
    for i in range(1, len(job_sections), 4):  # Every 4th element is a job section
        if i + 3 >= len(job_sections):
            break
            
        title = job_sections[i].strip()
        company = job_sections[i + 1].strip()
        period = job_sections[i + 2].strip()
        content = job_sections[i + 3].strip()
        
        # Extract responsibilities and achievements
        responsibilities = []
        achievements = []
        
        lines = content.split('\n')
        current_section = ""
        
        for line in lines:
            line = line.strip()
            if line.startswith('**Key Responsibilities:**'):
                current_section = "responsibilities"
            elif line.startswith('**Notable Achievements:**'):
                current_section = "achievements"
            elif line.startswith('- ') and current_section == "responsibilities":
                responsibilities.append(line.replace('- ', ''))
            elif line.startswith('- ') and current_section == "achievements":
                achievements.append(line.replace('- ', ''))
        
        # Combine responsibilities and achievements
        all_items = responsibilities + achievements
        items_html = ''.join([f'<li>{item}</li>' for item in all_items[:6]])  # Limit to 6 items
        
        experience_html += f'''
        <div class="experience-item">
            <div class="experience-header">
                <h3>{title}</h3>
                <div class="experience-meta">{company} | {period}</div>
            </div>
            <div class="experience-achievements">
                <ul>
                    {items_html}
                </ul>
            </div>
        </div>
        '''
    
    return experience_html

def extract_contact_info(contact_content):
    """Extract contact information"""
    contact_info = {
        'email': 'your.email@example.com',
        'linkedin': 'https://linkedin.com/in/yourprofile',
        'github': 'https://github.com/yourusername'
    }
    
    # Extract email
    email_match = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', contact_content)
    if email_match:
        contact_info['email'] = email_match.group()
    
    # Extract LinkedIn
    linkedin_match = re.search(r'linkedin\.com/in/[\w-]+', contact_content)
    if linkedin_match:
        contact_info['linkedin'] = 'https://' + linkedin_match.group()
    
    # Extract GitHub
    github_match = re.search(r'github\.com/[\w-]+', contact_content)
    if github_match:
        contact_info['github'] = 'https://' + github_match.group()
    
    return contact_info

def main():
    """Main conversion function"""
    if len(sys.argv) != 2:
        print("Usage: python convert-markdown.py <markdown-file>")
        sys.exit(1)
    
    markdown_file = sys.argv[1]
    
    if not os.path.exists(markdown_file):
        print(f"Error: Markdown file '{markdown_file}' not found.")
        sys.exit(1)
    
    print("🔄 Converting Markdown portfolio to HTML...")
    
    # Read markdown content
    markdown_content = read_file(markdown_file)
    
    # Extract sections
    sections = extract_sections(markdown_content)
    
    # Read HTML template
    template_html = read_file('index.html')
    
    # Parse sections
    about_html = convert_markdown_to_html(sections['about'])
    skills_html = parse_skills(sections['skills'])
    projects_html = parse_projects(sections['projects'])
    experience_html = parse_experience(sections['experience'])
    contact_info = extract_contact_info(sections['contact'])
    
    # Replace placeholders in template
    html_content = template_html.replace(
        '<!-- Your About Me content will go here -->',
        about_html
    ).replace(
        '<!-- Skills will be dynamically inserted here -->',
        skills_html
    ).replace(
        '<!-- Projects will be dynamically inserted here -->',
        projects_html
    ).replace(
        '<!-- Experience will be dynamically inserted here -->',
        experience_html
    ).replace(
        'your.email@example.com',
        contact_info['email']
    ).replace(
        'https://linkedin.com/in/yourprofile',
        contact_info['linkedin']
    ).replace(
        'https://github.com/yourusername',
        contact_info['github']
    )
    
    # Extract name from markdown for title
    name_match = re.search(r'# (.*?) Portfolio', markdown_content)
    if name_match:
        name = name_match.group(1)
        html_content = html_content.replace('Your Name', name)
    
    # Write output files
    write_file('index.html', html_content)
    
    print("✅ Conversion completed successfully!")
    print("📁 Files created:")
    print("   - index.html (main portfolio page)")
    print("   - style.css (already exists)")
    print("   - script.js (already exists)")
    print("\n🚀 Ready to deploy to GitHub Pages!")

if __name__ == "__main__":
    main()
