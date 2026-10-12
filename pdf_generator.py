import os
import re
from jinja2 import Template
from playwright.sync_api import sync_playwright

def generate_pdf(cv_data, template_path, output_pdf_path, language="en"):
    print("[*] Optimize edilmiş ATS uyumlu PDF oluşturuluyor (Playwright Headless Engine)...")

    with open(template_path, "r", encoding="utf-8") as f:
        template_content = f.read()

    template = Template(template_content)
    labels = {
        "az": {
            "summary": "Peşəkar xülasə", "experience": "İş təcrübəsi",
            "projects": "Layihələr", "view_project": "Layihəyə bax",
            "education": "Təhsil", "skills": "Texniki bacarıqlar",
            "certifications": "Sertifikatlar",
        },
        "en": {
            "summary": "Professional Summary", "experience": "Work Experience",
            "projects": "Projects & Engineering Work", "view_project": "View Project",
            "education": "Education", "skills": "Technical Skills",
            "certifications": "Certifications",
        },
    }
    render_data = dict(cv_data)
    certifications = render_data.get("certifications", [])
    certification_items = certifications if isinstance(certifications, list) else [certifications]
    render_data["certifications"] = [
        part.strip()
        for item in certification_items
        if isinstance(item, str)
        for part in re.split(r"[|\n]+", item)
        if part.strip()
    ]
    rendered_html = template.render(**render_data, labels=labels.get(language, labels["en"]), language=language)

    os.makedirs(os.path.dirname(output_pdf_path), exist_ok=True)

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page()
            page.set_content(rendered_html)

            page.wait_for_timeout(500) 

            page.pdf(path=output_pdf_path, format="A4", print_background=True)

        return True
    except Exception as e:
        print(f"[!] PDF oluşturulurken hata: {e}")
        return False
