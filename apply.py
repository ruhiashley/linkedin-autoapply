from dotenv import load_dotenv
from browser_use import Agent, Browser, BrowserProfile
from langchain_anthropic import ChatAnthropic
import asyncio
import random

load_dotenv()

MY_INFO = """
Full Name: Ruhi Ashley
Email: ruhiashley1@gmail.com
Phone: (952) 212-6074
Location: Dallas, TX
University: Texas A&M University - College Station
Degree: Bachelor of Science in Data Engineering
Graduation Date: May 2027
LinkedIn: linkedin.com/in/ruhi-ashley
Resume path: /Users/ruhischool/Downloads/Ruhi_Ashley_resume.pdf
Current Role: Software Development Intern
Years of Experience: 1.5
Programming Languages: Python, JavaScript, SQL, C++
Frameworks: React, Node.js, Express.js, Next.js
Tools: GitHub, GitHub Actions, Postman, MySQL Workbench
Cloud: AWS (EC2, S3, RDS, Lambda, CloudFront, API Gateway)
Certifications: AWS Certified AI Practitioner (AIF), AWS Certified Cloud Practitioner (CLF)
"""

RESUME_PATH = "/Users/ruhischool/Downloads/Ruhi_Ashley_resume.pdf"

SEARCH_TERMS = [
    "Cloud Engineering Intern",
    "Software Engineering Intern",
    "Data Engineering Intern",
    "DevOps Intern",
    "AWS Intern",
    "Backend Engineering Intern",
    "Software Developer Intern",
    "Full Stack Intern",
    "Full Stack Developer Intern",
    "Cloud Infrastructure Intern",
    "Site Reliability Engineer Intern",
    "Platform Engineering Intern",
    "MLOps Intern",
    "Data Analyst Intern",
    "Data Science Intern",
    "AI Engineering Intern",
    "Machine Learning Intern",
    "Junior Software Engineer Intern",
    "React Developer Intern",
    "Node.js Developer Intern",
    "Software Development Intern",
    "Web Developer Intern",
    "Cloud Developer Intern",
    "Infrastructure Intern",
    "Solutions Engineer Intern",
    "Database Engineer Intern",
    "API Developer Intern",
]

random.shuffle(SEARCH_TERMS)


async def apply_for_term(term: str, browser: Browser):
    task = f"""
Go to https://www.linkedin.com/jobs/
Search for "{term}" in "United States".
Apply these filters:
- Easy Apply only
- Experience level: Internship
- Date posted: Past month
Apply to the first 3 Easy Apply jobs you find.
Use this info to fill out all forms:
{MY_INFO}
Rules:
- Only apply to jobs with the Easy Apply button
- Skip any job that opens an external website
- Skip any job that requires a cover letter
- Do not apply to the same company twice
- If there is a resume upload field, upload the resume at: {RESUME_PATH}
- After applying to 3 jobs, stop and return
"""
    agent = Agent(
        task=task,
        llm=ChatAnthropic(model="claude-sonnet-4-6"),
        browser=browser,
        available_file_paths=[RESUME_PATH],
    )
    await agent.run()


async def main():
    browser = Browser(
        BrowserProfile(
            executable_path="/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            user_data_dir="~/Library/Application Support/Google/Chrome",
            profile_directory="Default",
            keep_alive=True,
            headless=False,
        )
    )

    for term in SEARCH_TERMS:
        print(f"\nSearching: {term}")
        try:
            await apply_for_term(term, browser)
        except Exception as e:
            print(f"Error on '{term}': {e} -- skipping to next")
        await asyncio.sleep(random.uniform(3, 8))

    await browser.close()
    print("\nDone applying!")


if __name__ == "__main__":
    asyncio.run(main())
