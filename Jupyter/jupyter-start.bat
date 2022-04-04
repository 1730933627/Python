@echo off
cd ../
jupyter notebook   --NotebookApp.allow_origin='https://colab.research.google.com'   --port=8888   --NotebookApp.port_retries=0  --NotebookApp.token=12345678 --NotebookApp.open_browser=False