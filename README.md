# AI Agent App

A full-stack application with a React frontend and FastAPI backend, designed to be deployed on Vercel.

## Project Structure

```
ai-agent-app/
├── api/                # Backend FastAPI server
│   └── main.py        # Main API entry point
├── frontend/          # React frontend application
│   ├── src/          # Source code
│   ├── public/       # Static assets
│   └── package.json  # Frontend dependencies
├── requirements.txt   # Python dependencies
└── vercel.json       # Vercel deployment configuration
```

## Prerequisites

- Node.js (v18 or higher)
- Python (v3.8 or higher)
- Git

## Local Development Setup

### Backend Setup

1. Create and activate a virtual environment:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install Python dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory:

   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. Start the backend server:
   ```bash
   cd api
   uvicorn main:app --reload
   ```

### Frontend Setup

1. Install Node.js dependencies:

   ```bash
   cd frontend
   npm install
   ```

2. Start the development server:
   ```bash
   npm run dev
   ```

The frontend will be available at `http://localhost:5173` and the backend at `http://localhost:8000`.

## API Documentation

Once the backend server is running, you can access:

- Swagger UI documentation: `http://localhost:8000/docs`
- ReDoc documentation: `http://localhost:8000/redoc`

## Available Scripts

### Backend

- `uvicorn main:app --reload`: Start the development server
- `uvicorn main:app`: Start the production server

### Frontend

- `npm run dev`: Start the development server
- `npm run build`: Build for production
- `npm run preview`: Preview production build
- `npm run lint`: Run ESLint

## Deployment

This project is configured for deployment on Vercel. The `vercel.json` file handles:

- Building both frontend and backend
- Routing API requests to the Python server
- Serving the frontend static files

### Deployment Steps

1. Push your code to GitHub
2. Connect your repository to Vercel
3. Configure environment variables in the Vercel dashboard
4. Deploy!

## Environment Variables

### Backend (.env)

```
PORT=8000
# Add other backend environment variables
```

### Frontend (.env)

```
VITE_API_URL=http://localhost:8000
# Add other frontend environment variables
```

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.
