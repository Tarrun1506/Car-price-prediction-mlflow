import os
import sys

port = os.environ.get('PORT', '8501')
os.environ['STREAMLIT_SERVER_PORT'] = port
os.environ['STREAMLIT_SERVER_ADDRESS'] = '0.0.0.0'

from streamlit.web.cli import main

sys.argv = ['streamlit', 'run', 'app.py']
raise SystemExit(main())
