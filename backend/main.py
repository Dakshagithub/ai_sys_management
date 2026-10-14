from fastapi import FastAPI

app = FastAPI(
    title="AI System Monitor",
    description="AI-powered system monitoring and incident assistant",
    version="0.1.0",
)


@app.get("/api/health")
def health_check():
    return {
        "status": "healthy",
        "service": "ai-system-monitor",
    }