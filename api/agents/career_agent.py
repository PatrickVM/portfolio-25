from agents.base_agent import BaseAgent


class CareerAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="CareerGuide",
            description="I'm the career specialist. I can provide information about skills, experience, and job suitability.",
            avatar="career_avatar.png"
        )

        self.skills = {
            "languages": ["Python", "JavaScript", "TypeScript", "Postgres", "SQL"],
            "frameworks": ["React", "Next.js", "Node.js", "Django", "Flask"],
            "tools": ["Git", "Docker", "AWS", "Digital Ocean", "NeonDB", "Prisma", "Sanity", "Socket.io", "Clerk"],
            "soft_skills": ["Team leadership", "Project management", "Community building", "Ratchet-Imagineering"]
        }

        self.experience = [
            {
                "title": "Full Stack Developer",
                "company": "ARC",
                "period": "2022-Present",
                "responsibilities": [
                    "Build internal tools to help the company run more efficiently",
                    "Work with team of 6 to build and maintain ARC Internal Apps.",
                    "Implement AI-solutions that keeps privacy in high-priority",
                    "Architected microservices infrastructure"
                ]
            },
            {
                "title": "Full Stack Developer",
                "company": "Freelancer",
                "period": "2019-Present",
                "responsibilities": [
                    "Developed responsive web applications using React and Node.js",
                    "Implemented RESTful APIs and database schemas",
                    "Assist in technical advice and support",
                    "Participated in open-source projects"
                ]
            },
            {
                "title": "Junior Developer",
                "company": "Kj Services",
                "period": "2020-2021",
                "responsibilities": [
                    "Maintain internal tools for the company",
                    "Develop in C#",
                    "Assisted in database design and optimization"
                ]
            }
        ]

    def get_skills_summary(self):

        prompt = f"""
        Generate a professional summary of the following skills for a portfolio website:

        Programming Languages: {', '.join(self.skills['languages'])}
        Frameworks & Libraries: {', '.join(self.skills['frameworks'])}
        Tools & Platforms: {', '.join(self.skills['tools'])}
        Soft Skills: {', '.join(self.skills['soft_skills'])}

        Format the response in markdown with appropriate sections and highlights.
        """
        return self.get_response(prompt)

    def get_experience_summary(self):

        experience_text = "# Work Experience\n\n"
        for job in self.experience:
            experience_text += f"## {job['title']} at {job['company']}\n"
            experience_text += f"**{job['period']}**\n\n"
            experience_text += "**Responsibilities:**\n"
            for resp in job['responsibilities']:
                experience_text += f"- {resp}\n"
            experience_text += "\n"

        prompt = f"""
        Based on the following work experience, generate a professional career summary for a portfolio website:

        {experience_text}

        Highlight career progression, key achievements, and growth. Format the response in markdown.
        """
        return self.get_response(prompt)

    def assess_job_fit(self, job_description):

        skills_flat = []
        for skill_category in self.skills.values():
            skills_flat.extend(skill_category)

        experience_flat = []
        for job in self.experience:
            experience_flat.extend(job['responsibilities'])

        prompt = f"""
        Assess the fit for the following job description based on the skills and experience provided:

        Job Description:
        {job_description}

        Skills:
        {', '.join(skills_flat)}

        Experience:
        {' '.join(experience_flat)}

        Provide an analysis of strengths, potential gaps, and overall suitability for the role. Format the response in markdown.
        """
        return self.get_response(prompt)