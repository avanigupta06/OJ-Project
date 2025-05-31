# import google.generativeai as genai
# from django.conf import settings

# def get_code_review(code, problem_desc):
#     if not code.strip():
#         return "You have not written any code."
    
#     genai.configure(api_key=settings.GEMINI_API_KEY)
#     model = genai.GenerativeModel("gemini-2.0-flash")
#     prompt = f"""
# You are a code reviewer. Given the following problem description and code:

# Problem:
# {problem_desc}

# Code:
# {code}

# Provide a **short**, plain-text review (under 100 words) with:
# - Key feedback
# - Suggestions for improvement
# - Mention edge cases if needed

# Do NOT include code snippets or examples. Avoid using stars, bullet points, or markdown formatting.
#     """


#     try:
#         response = model.generate_content(prompt)
#         return response.text
#     except Exception as e:
#         return f"AI Review Error: {str(e)}"
