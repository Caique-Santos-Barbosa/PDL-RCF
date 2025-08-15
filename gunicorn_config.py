"""
Configuração do Gunicorn para produção no Render
"""
import multiprocessing

# Configurações básicas
bind = "0.0.0.0:10000"
workers = multiprocessing.cpu_count() * 2 + 1
worker_class = "gevent"
worker_connections = 1000
timeout = 30
keepalive = 2

# Configurações de logging
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Configurações de segurança
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190

# Configurações de performance
max_requests = 1000
max_requests_jitter = 50
preload_app = True

# Configurações específicas para WebSocket
worker_tmp_dir = "/dev/shm"

# Configurações de timeout
graceful_timeout = 30 