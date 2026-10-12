import time
from datetime import datetime

from scraper import scrape_job_description
from ai_optimizer import CVOptimizer
from pdf_generator import generate_pdf
from docx_generator import generate_docx
from cv_parser import parse_pdf_to_json
from file_io import load_json, load_text
from output_paths import build_run_output_paths

def main():
    print("--- Çift Dilli ATS Bypass Sistemi Başlatılıyor ---")
    
    try:
        config = load_json("config.json")
    except FileNotFoundError:
        print("[!] HATA: config.json dosyası bulunamadı.")
        return

    raw_pdf = config.get("RAW_CV_PATH")
    if raw_pdf:
        print("[*] Ham PDF CV algılandı, işleniyor...")
        parse_pdf_to_json(
            pdf_path=raw_pdf, 
            output_json_path=config["BASE_CV_PATH"], 
            api_key=config["GEMINI_API_KEY"]
        )

    base_cv = load_json(config["BASE_CV_PATH"])
    
    job_desc_text = scrape_job_description(config["TARGET_JOB_URL"])
    time.sleep(0.5) 
    
    if not job_desc_text or len(job_desc_text.strip()) < 50:
        print("\n[!] Anti-Bot Koruması Tespit Edildi.")
        print("[*] 'Manual Override' (ilan.txt üzerinden veri enjeksiyonu) başlatılıyor...")
        try:
            job_desc_text = load_text("ilan.txt")
            print("[✔] İlan metni yerel dosyadan (ilan.txt) yüklendi!\n")
        except Exception as e:
            print(f"[✘] Kritik Hata: 'ilan.txt' okunamadı. ({e})")
            return

    optimizer = CVOptimizer(api_key=config["GEMINI_API_KEY"])
    bilingual_cv = optimizer.optimize_bilingual(base_cv, job_desc_text)
    
    if not bilingual_cv or "az" not in bilingual_cv or "en" not in bilingual_cv:
        print("[✘] Çift dilli optimizasyon başarısız oldu.")
        return

    bilingual_cv['az']['title'] = base_cv.get('title', 'Software Engineer')
    bilingual_cv['en']['title'] = base_cv.get('title', 'Software Engineer')
    print("\n" + "=" * 50)
    print("🔥 YAPAY ZEKA OPTİMİZASYON RAPORU (AZ & EN)")
    print("=" * 50)
    
    print("\n🇦🇿 [AZƏRBAYCAN DİLİ VERSİYASI]")
    print(f"• Bacarıqlar:\n  {bilingual_cv['az'].get('skills')}")
    print(f"• İlk iş təcrübəsinin təsviri:\n  {bilingual_cv['az'].get('experience')[0].get('description')}")
    
    print("\n🇬🇧 [İNGİLİZCE VERSİYON]")
    print(f"• Skills:\n  {bilingual_cv['en'].get('skills')}")
    print(f"• First Experience Description:\n  {bilingual_cv['en'].get('experience')[0].get('description')}")
    
    print("=" * 50 + "\n")
    time.sleep(0.5)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_paths = build_run_output_paths(config["OUTPUT_PDF_PATH"], timestamp)

    success_az_pdf = generate_pdf(bilingual_cv['az'], config["TEMPLATE_PATH"], output_paths["az_pdf"], language="az")
    success_en_pdf = generate_pdf(bilingual_cv['en'], config["TEMPLATE_PATH"], output_paths["en_pdf"], language="en")
    success_az_docx = generate_docx(bilingual_cv['az'], output_paths["az_docx"], language="az")
    success_en_docx = generate_docx(bilingual_cv['en'], output_paths["en_docx"], language="en")

    if success_az_pdf and success_en_pdf and success_az_docx and success_en_docx:
        print(f"\n[✔] İŞLEM TAMAM!")
        print(f"   - Klasör: {output_paths['run_dir']}")
        print(f"   - Azərbaycanca PDF: {output_paths['az_pdf']}")
        print(f"   - İngilizce PDF: {output_paths['en_pdf']}")
        print(f"   - Azərbaycanca DOCX: {output_paths['az_docx']}")
        print(f"   - İngilizce DOCX: {output_paths['en_docx']}")
    else:
        print("[✘] Cikti dosyalari uretilirken hata olustu.")

if __name__ == "__main__":
    main()
