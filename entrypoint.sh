#!/bin/bash

exec gunicorn -w 3 -t 120 --max-requests 75 -b 0.0.0.0:8000 auto_churn.wsgi:application