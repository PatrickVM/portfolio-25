from agents.base_agent import BaseAgent


class ProjectAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            name="TechExpert",
            description="I'm the project specialist. I can provide detailed information about any project in this portfolio.",
            avatar="project_avatar.png"
        )

        self.projects = {
            "project1": {
                "name": "Exchange Platform",
                "tech_stack": ["React", "Nextjs", "NeonDB", "Prisma", "TailwindCSS", "Socket.io", "Digital Ocean"],
                "description": "A full-stack Exchange platform with user authentication, contracts, public profiles, realtime chat, and sleek design.",
                "highlights": ["Responsive design", "authentication", "realtime updates", "creative possibilities"],
                "github_link": "request link",
                "demo_link": "https://bartr.tech/"
            },
            "project2": {
                "name": "LMS for Voyage Church",
                "tech_stack": ["Nextjs", "Sanity", "Tailwind CSS", "Node.js", "Clerk"],
                "description": "A learning management system for Voyage Church.",
                "highlights": ["Landing Page", "Easy to use", "Sleek Design", "Progressive Web App", "Stripe Integration"],
                "github_link": "https://github.com/PatrickVM/vc-lms",
                "demo_link": "https://www.thevoyage.us/"
            }
        }

    def get_project_list(self):

        project_list = "# Available Projects\n\n"
        for project_id, project in self.projects.items():
            project_list += f"## {project['name']}\n"
            project_list += f"**Tech Stack**: {', '.join(project['tech_stack'])}\n"
            project_list += f"{project['description']}\n\n"

        return project_list

    def get_project_details(self, project_id):

        if project_id in self.projects:
            project = self.projects[project_id]
            prompt = f"""
            Generate a detailed description for the following project:

            Project Name: {project['name']}
            Tech Stack: {', '.join(project['tech_stack'])}
            Description: {project['description']}
            Highlights: {', '.join(project['highlights'])}
            GitHub: {project['github_link']}
            Demo: {project['demo_link']}

            Include technical details about implementation challenges and solutions. Format the response in markdown.
            """
            return self.get_response(prompt)
        else:
            return "Project not found. Please check the project ID and try again."

    def answer_technical_question(self, project_id, question):

        if project_id in self.projects:
            project = self.projects[project_id]
            prompt = f"""
            Answer the following technical question about this project:

            Project Name: {project['name']}
            Tech Stack: {', '.join(project['tech_stack'])}
            Description: {project['description']}
            Highlights: {', '.join(project['highlights'])}

            Question: {question}

            Provide a detailed technical answer with code examples if relevant.
            """
            return self.get_response(prompt)
        else:
            return "Project not found. Please check the project ID and try again."