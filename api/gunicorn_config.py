import multiprocessing
import os

# Server socket
bind = "0.0.0.0:" + os.getenv("PORT", "8000")
backlog = 2048

# Worker processes
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

# Logging
accesslog = "-"  # stdout
errorlog = "-"   # stderr
loglevel = "info"

# Process naming
proc_name = "ai-agent-api"

# SSL (uncomment and configure if using HTTPS)
# keyfile = "path/to/keyfile"
# certfile = "path/to/certfile"

# Server mechanics
daemon = False
pidfile = None
umask = 0
user = None
group = None
tmp_upload_dir = None

# Server hooks
def on_starting(server):
    """
    Called just before the master process is initialized.
    """
    pass

def on_reload(server):
    """
    Called to recycle workers during a reload via SIGHUP.
    """
    pass

def post_fork(server, worker):
    """
    Called just after a worker has been forked.
    """
    server.log.info("Worker spawned (pid: %s)", worker.pid)

def pre_fork(server, worker):
    """
    Called just prior to forking the worker subprocess.
    """
    pass

def pre_exec(server):
    """
    Called just prior to forking a new master process during a reload.
    """
    server.log.info("Forked master process, reloading") 