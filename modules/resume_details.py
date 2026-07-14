from pypdf import PdfReader


def get_resume_details(pdf_file, resume_text):
    reader = PdfReader(pdf_file)

    details = {
        "file_name": pdf_file.name,
        "file_size": round(pdf_file.size / 1024, 2),
        "pages": len(reader.pages),
        "characters": len(resume_text),
        "words": len(resume_text.split())
    }

    return details