import google.generativeai as genai
from django.conf import settings

def get_code_review(code, problem_desc):
    if not code.strip():
        return "You have not written any code."
    
    genai.configure(api_key=settings.GEMINI_API_KEY)
    model = genai.GenerativeModel("gemini-2.0-flash")
    prompt = f"""You are a code reviewer. Analyze the following code and problem description.
    
    Give concise review of the code. Also, provide a list of potential improvements, suggestions for the code and edge cases if any.
    Do not use any markdown symbols like **, *, or ```.

    Problem:
    {problem_desc}
    
    Code:
    {code}
    """


    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"AI Review Error: {str(e)}"
