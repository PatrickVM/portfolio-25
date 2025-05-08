# AI Agent Portfolio App

A full-stack application featuring an AI-powered portfolio website with a React frontend and Flask backend, designed for deployment on Vercel.

## Project Structure

```
ai-agent-app/
├── venv/                # Backend code and virtual environment
│   ├── main.py         # Main Flask application
│   ├── agents/         # AI agent implementations
│   │   ├── base_agent.py
│   │   ├── welcome_agent.py
│   │   ├── project_agent.py
│   │   ├── career_agent.py
│   │   ├── client_agent.py
│   │   └── research_agent.py
│   └── ...
├── frontend/           # React frontend
│   ├── src/
│   ├── public/
│   └── package.json
├── .env.example        # Example environment variables
├── .gitignore         # Git ignore rules
├── requirements.txt    # Python dependencies
└── vercel.json        # Vercel configuration
```

## Prerequisites

- Node.js (v18 or higher)
- Python (v3.8 or higher)
- Vercel CLI (for deployment)
- Groq API key

## Local Development Setup

### Backend Setup

1. Navigate to the project root:

   ```bash
   cd ai-agent-app
   ```

2. Create and activate a Python virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the root directory:

   ```bash
   cp .env.example .env
   ```

   Then edit `.env` and add your Groq API key.

5. Start the Flask development server:
   ```bash
   cd venv
   flask run
   ```
   The backend will be available at `http://localhost:5000`

### Frontend Setup

1. Navigate to the frontend directory:

   ```bash
   cd frontend
   ```

2. Install Node.js dependencies:

   ```bash
   npm install
   ```

3. Start the development server:
   ```bash
   npm run dev
   ```
   The frontend will be available at `http://localhost:5173`

## Available Scripts

### Backend

- `flask run`: Start the Flask development server
- `flask test`: Run backend tests (if implemented)

### Frontend

- `npm run dev`: Start the development server
- `npm run build`: Build for production
- `npm run preview`: Preview the production build
- `npm run lint`: Run ESLint

## API Documentation

Once the backend server is running, you can access the API documentation at:

- Swagger UI: `http://localhost:5000/api/docs`
- ReDoc: `http://localhost:5000/api/redoc`

## Deployment

### Vercel Deployment

1. Install Vercel CLI:

   ```bash
   npm install -g vercel
   ```

2. Deploy to Vercel:

   ```bash
   vercel
   ```

3. Configure environment variables in the Vercel dashboard:
   - `GROQ_API_KEY`: Your Groq API key
   - `FLASK_ENV`: Set to "production"

### Environment Variables

Required environment variables:

- `GROQ_API_KEY`: Your Groq API key for AI agent functionality
- `FLASK_ENV`: Environment setting (development/production)
- `FLASK_APP`: Path to the Flask application (venv/main.py)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
