#!/bin/bash
export PORT=8001
gunicorn api.wsgi:app