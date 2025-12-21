# Standard imports
import os
import json
from pathlib import Path
from typing import Dict, List
from google import genai
from google.genai import types
from langfuse import observe


class AIService:
    """Service for all AI operations using Gemini."""

    def __init__(self, model: str = "gemini-2.5-flash-lite"):
        self.client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))
        self.model = model

    @observe()
    def process_pdf(self, pdf_bytes, prompt: str = "Extract all text from this document") -> str:

        
        # Send to Gemini with prompt
        response = self.client.models.generate_content(
            model=self.model,
            contents=[
                prompt,
                types.Part.from_bytes(
                    data=pdf_bytes,
                    mime_type='application/pdf'
                )
            ]
        )
        
        return response.text
    
    @observe()

    def generate_summary(self, document_text: str, summary_type: str, length: str) -> str:
        prompt_map = {
              "Bullet points": f"Summarize the document as bullet points. Keep it {length.lower()}.",
              "Key takeaways": f"Give the key takeaways from the document. Keep it {length.lower()}.",
              "Overview paragraph": f"Write a clear overview paragraph of the document. Keep it {length.lower()}.",
              "Key terms": f"Extract important key terms and define each briefly. Keep it {length.lower()}.",
              "Section-by-section": f"Summarize the document section-by-section with short bullets per section. Keep it {length.lower()}."
        }
        
        prompt = prompt_map.get(summary_type)
       
        
        response = self.client.models.generate_content(
            model= self.model,
            contents=[prompt, document_text],
        )
        
        return response.text
    
    def question_answer(self, document_text, user_question) -> str:
        # Send to Gemini with prompt
        response = self.client.models.generate_content(
            model=self.model,
            contents=f"""
                Document:
                {document_text}

                Question:
                {user_question}

                Answer concisely using context from the document and outside knowledge if appropriate:
                """
        )
        
        return response.text


    def generate_quiz(self, document_text: str, num_questions: int):
        prompt = f"""
Create {num_questions} multiple-choice questions based ONLY on the document.

Return ONLY a Python list of dictionaries (no extra text), exactly like:

[
  {{
    "question": "text",
    "options": {{"A":"...", "B":"...", "C":"...", "D":"..."}},
    "answer": "A",
    "explanation": "1-2 sentences"
  }}
]

Rules:
- 4 options A-D
- answer must be one of A/B/C/D
- explanation must justify why the correct answer is correct
"""

        response = self.client.models.generate_content(
            model= self.model,
            contents=[prompt, document_text],
        )

        # Convert text -> Python list safely
        return ast.literal_eval(resp.text.strip())








