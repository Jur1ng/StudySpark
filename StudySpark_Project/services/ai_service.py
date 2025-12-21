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

    def generate_summary(self, document_text: str, prompt: str) -> str:
        response = self.client.models.generate_content(
            model= self.model,
            contents=[prompt, document_text],
        )

        # IMPORTANT: return the text
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
        

