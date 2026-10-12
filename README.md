## 🚀 ATS CV Optimizer

AI-Powered CV Optimization for Applicant Tracking Systems (ATS)

ATS CV Optimizer is an AI-powered tool designed to tailor your CV to specific job descriptions. It analyzes your existing CV, extracts relevant information from job postings, and generates optimized CV documents in PDF and DOCX formats.

The goal is to help job seekers present their skills and experience more effectively while maintaining the accuracy of their professional background.

Languages: Azərbaycan dili (AZ) · English (EN)

🌍 Languages / Dillər
Azərbaycan dili
English
🇦🇿 Azərbaycanca
📌 Layihə haqqında

ATS CV Optimizer — CV-nizi konkret vakansiyaya uyğunlaşdırmaq üçün hazırlanmış süni intellekt əsaslı alətdir.

Bir çox şirkət CV-ləri ilkin mərhələdə Applicant Tracking System (ATS) adlı namizəd izləmə sistemləri vasitəsilə emal edir. Bu layihə CV-nizin vakansiyada tələb olunan bacarıq və təcrübələri daha aydın ifadə etməsinə kömək edir.

Layihə mövcud CV məlumatlarını təhlil edir, vakansiya mətnini əldə edir və uyğunlaşdırılmış CV sənədləri yaradır.

✨ Əsas imkanlar
🤖 Süni intellektlə optimallaşdırma: CV məzmununun vakansiyanın tələblərinə uyğunlaşdırılmasına kömək edir.
🎯 Vakansiyaya uyğunlaşdırma: İş elanındakı tələbləri və əsas bacarıqları nəzərə alır.
📄 PDF və DOCX ixracı: Nəticələri iki geniş istifadə olunan sənəd formatında yaradır.
🌐 Çoxdilli CV dəstəyi: Layihənin mövcud versiyasında türk və ingilis dillərində CV yaradılması nəzərdə tutulub. Azərbaycan dili dəstəyi əlavə edilən versiyada bu bölməni faktiki imkanlara uyğun saxlayın.
🔎 Vakansiya məlumatlarının əldə edilməsi: İş elanı URL-indən məlumat toplamağa çalışır.
🛠️ Alternativ vakansiya mətni: Avtomatik məlumat əldə etmək mümkün olmadıqda ilan.txt faylından istifadə edə bilər.
📂 Nəticələrin təşkili: Yaradılmış fayllar ayrıca çıxış qovluğunda saxlanıla bilər.
🧰 İstifadə olunan texnologiyalar
Python
Google Gemini API
Streamlit
Playwright
Beautiful Soup
Jinja2
PyPDF
python-docx
⚙️ Quraşdırma
1. Repozitorini klonlayın
git clone https://github.com/aghabalaguluzade/ATS-CV-Optimizer-AZ-EN.git
cd Ats-Cv-Optimizer


2. Virtual mühit yaradın

Windows:

python -m venv .venv
.venv\Scripts\activate


Linux / macOS:

python3 -m venv .venv
source .venv/bin/activate

3. Asılılıqları quraşdırın
python -m pip install --upgrade pip
pip install -r requirements.txt

4. API açarını konfiqurasiya edin

Google Gemini API açarı əldə edin və config.example.json faylını əsas götürərək config.json yaradın.

Nümunə konfiqurasiya:

{
  "GEMINI_API_KEY": "YOUR_GEMINI_API_KEY",
  "TARGET_JOB_URL": "https://example.com/job-posting",
  "BASE_CV_PATH": "data/your_cv.json",
  "TEMPLATE_PATH": "template.html",
  "OUTPUT_PDF_PATH": "output/optimized_cv.pdf",
  "RAW_CV_PATH": "data/your_raw_cv.pdf"
}


Fayl yollarını öz layihə strukturunuza uyğunlaşdırın. BASE_CV_PATH mövcud CV məlumatlarını saxlayan JSON faylına, RAW_CV_PATH isə ilkin PDF CV faylına işarə etməlidir.

5. CV və vakansiya məlumatlarını hazırlayın
CV-nizi konfiqurasiyada göstərilən yola yerləşdirin.
Vakansiyanın URL-ni TARGET_JOB_URL sahəsinə yazın.
Göstərilən fayl yollarının mövcud olduğuna əmin olun.
▶️ Layihənin işə salınması

Əsas proqramı işə salmaq üçün:

python -m streamlit run dashboard.py 


Proqram konfiqurasiya faylını oxuyur, CV və vakansiya məlumatlarını emal edir, AI vasitəsilə CV məzmununu optimallaşdırır və PDF/DOCX sənədlərini yaratmağa çalışır.

📁 Layihənin strukturu
```
Ats-Cv-Optimizer/
├── ai_optimizer.py
├── cv_change_tracker.py
├── cv_parser.py
├── dashboard.py
├── dashboard_service.py
├── docx_generator.py
├── file_io.py
├── main.py
├── output_paths.py
├── path_utils.py
├── pdf_generator.py
├── prompt.json
├── prompt_loader.py
├── scraper.py
├── template.html
├── config.example.json
├── requirements.txt
└── README.md
```

📤 Nəticə

Proqram uğurla tamamlandıqda CV-nin optimallaşdırılmış versiyaları PDF və DOCX formatlarında yaradılır. Faylların dəqiq adları və saxlanma yeri konfiqurasiyadan asılıdır.

⚠️ Vacib qeydlər
ATS uyğunlaşdırılması müsahibəyə çağırılmağa və ya işə qəbul olunmağa zəmanət vermir.
AI tərəfindən yaradılmış məzmunu göndərməzdən əvvəl yoxlayın.
CV-də olmayan bacarıq, təcrübə və nailiyyətləri əlavə etməyin.
Bəzi vakansiya saytları avtomatik məlumat toplanmasını məhdudlaşdıra bilər.
API istifadəsi ödənişli ola bilər; provayderin şərtlərini yoxlayın.
🤝 Töhfə

Layihəni inkişaf etdirmək istəyirsinizsə:

Repozitorini fork edin.
Yeni branch yaradın.
Dəyişikliklərinizi edin və test edin.
Pull Request göndərin.
📄 Lisenziya

Bu layihəyə lisenziya əlavə ediləcəksə, burada müvafiq lisenziyanın adı və şərtləri göstərilməlidir.

🇦🇿 Təşəkkür və mənbə

Bu layihə Niyazi Cancinkir tərəfindən hazırlanmış Ats-Cv-Optimizer layihəsi əsasında hazırlanır.

Orijinal layihə bu versiyanın əsasını təşkil edir. Bu repozitorinin məqsədi layihəni Azərbaycan və ingilis dilləri üçün uyğunlaşdırmaq, dil dəstəyini genişləndirmək və əlavə təkmilləşdirmələr etməkdir.

İlkin layihəyə və onun əsas işinə görə orijinal müəllifə təşəkkür edirik.

Orijinal repozitori: https://github.com/Niyazicancinkir/Ats-Cv-Optimizer


## 🇬🇧 English
📌 About the Project

ATS CV Optimizer is an AI-powered tool designed to tailor your CV to specific job descriptions.

Many companies use Applicant Tracking Systems (ATS) to process job applications. This project helps make your skills, qualifications, and professional experience more relevant and clearly presented for a target position.

It processes existing CV data, retrieves job description content, and generates tailored CV documents.

✨ Key Features
🤖 AI-powered optimization: Helps adapt CV content to a target job description.
🎯 Job-specific tailoring: Uses relevant job requirements and skills to guide the optimization process.
📄 PDF and DOCX export: Generates documents in two widely used formats.
🌐 Multilingual output: The existing implementation generates Turkish and English CVs. Additional Azerbaijani output requires the corresponding implementation to be added and tested.
🔎 Job description retrieval: Attempts to retrieve content from a job posting URL.
🛠️ Manual fallback: Supports loading job description text from ilan.txt when automatic retrieval fails.
📂 Organized output: Saves generated documents using the configured output paths.
🧰 Tech Stack
Python
Google Gemini API
Streamlit
Playwright
Beautiful Soup
Jinja2
PyPDF
python-docx
⚙️ Installation
1. Clone the repository
git clone https://github.com/aghabalaguluzade/ATS-CV-Optimizer-AZ-EN.git
cd Ats-Cv-Optimizer

2. Create a virtual environment

Windows:

python -m venv .venv
.venv\Scripts\activate


Linux / macOS:

python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies
python -m pip install --upgrade pip
pip install -r requirements.txt

4. Configure the API key

Obtain a Google Gemini API key and create a config.json file based on config.example.json.

Example configuration:

{
  "GEMINI_API_KEY": "YOUR_GEMINI_API_KEY",
  "TARGET_JOB_URL": "https://example.com/job-posting",
  "BASE_CV_PATH": "data/your_cv.json",
  "TEMPLATE_PATH": "template.html",
  "OUTPUT_PDF_PATH": "output/optimized_cv.pdf",
  "RAW_CV_PATH": "data/your_raw_cv.pdf"
}


Update the file paths to match your local project structure. BASE_CV_PATH should point to your existing CV data in JSON format, while RAW_CV_PATH should point to your original PDF CV.

5. Prepare your CV and job description
Place your CV at the configured path.
Set TARGET_JOB_URL to the target job posting.
Verify that all configured file paths exist.
▶️ Running the Project

Run the main application with:

python -m streamlit run dashboard.py

The application loads the configuration, processes the CV and job description, runs the AI optimization workflow, and attempts to generate the resulting PDF and DOCX files.

📁 Project Structure
```
Ats-Cv-Optimizer/
├── ai_optimizer.py
├── cv_change_tracker.py
├── cv_parser.py
├── dashboard.py
├── dashboard_service.py
├── docx_generator.py
├── file_io.py
├── main.py
├── output_paths.py
├── path_utils.py
├── pdf_generator.py
├── prompt.json
├── prompt_loader.py
├── scraper.py
├── template.html
├── config.example.json
├── requirements.txt
└── README.md
```

📤 Output

When execution completes successfully, the application generates optimized CV documents in PDF and DOCX formats. Exact filenames and output locations depend on the configured paths.

⚠️ Important Notes
ATS optimization does not guarantee interviews or employment.
Review all AI-generated content before submitting your CV.
Never add skills, qualifications, or achievements that you do not possess.
Some job websites may restrict automated content retrieval.
API usage may incur costs; check the provider's current pricing and terms.
🤝 Contributing

Contributions are welcome!

Fork the repository.
Create a feature branch.
Implement and test your changes.
Submit a Pull Request.
📄 License

If you intend to distribute this project, add an appropriate license file and specify its name and terms here.

Built to make job applications more focused, clear, and effective.

🙏 Credits & Acknowledgements

This project is based on the original work by Niyazi Cancinkir in the Ats-Cv-Optimizer repository.

The original project served as the foundation for this version. This repository aims to extend and adapt the project with Azerbaijani and English language support, along with further improvements and customizations.

Full credit goes to the original author for the initial project and its underlying work.

Original repository: https://github.com/Niyazicancinkir/Ats-Cv-Optimizer
