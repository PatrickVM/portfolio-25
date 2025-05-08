# AI Agent Portfolio App

A portfolio website with AI-powered agents for different sections.

## Project Structure

```
ai-agent-app/
├── api/                 # Python backend
│   ├── main.py         # Main Flask application
│   ├── requirements.txt # Python dependencies
│   ├── gunicorn_config.py # Gunicorn configuration
│   └── run_prod.sh     # Production run script
├── frontend/           # React frontend
│   ├── src/           # Source files
│   └── package.json   # Node dependencies
└── vercel.json        # Vercel configuration
```

## Environment Variables

Create a `.env` file in the `api` directory with:

```
GROQ_API_KEY=your_groq_api_key_here
```

## Local Development

### Backend

```bash
cd api
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Production Deployment

1. Push to GitHub:

```bash
git add .
git commit -m "chore: prepare for production deployment"
git push origin main
```

2. Vercel will automatically deploy from the GitHub repository.

## API Endpoints

- `/api/welcome` - Welcome agent
- `/api/project` - Project information
- `/api/career` - Career information
- `/api/client` - Client services
- `/api/research` - Technology research

## Production Configuration

The application uses:

- Gunicorn as the WSGI server
- Multiple worker processes
- Proper logging configuration
- Error handling
- CORS support
- Environment variable management
