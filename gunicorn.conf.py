"""Gunicorn settings, picked up automatically when Render runs `gunicorn app:app` from this folder.
Flags on the start command still override these.

gunicorn's default is one worker that handles one request at a time with a 30 s timeout; at an
event every phone and overlay auto-refreshes, so requests queued up and slow ones got the worker
killed (looks like a crash). Threads let one worker serve several requests at once while keeping a
single process, so the in-memory page cache and its clearing stay consistent.
"""
workers = 1
worker_class = 'gthread'
threads = 8
timeout = 60           # seconds before a stuck request's worker is restarted
graceful_timeout = 30
keepalive = 5          # reuse connections from phones that refresh often
