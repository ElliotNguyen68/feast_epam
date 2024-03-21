# Init project
```bash
pip install -r requirements.txt
cd src/ && feast init my_project
cd my_project/feature_repo && feast apply
python test_workflow.py
feast ui
# http://0.0.0.0:8888

docker-compose up -d
```