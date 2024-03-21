# Init project
```bash
# Prepare PostgreSQL as Register
docker-compose up -d

# Install libraries
pip install -r requirements.txt
cd feature_repo && feast apply
python store.py
feast ui
# http://0.0.0.0:8888
```

# Start new feature_repo
```bash
feast init my_project
cd my_project/feature_repo
# feast apply
# OR: python test_workflow.py
feast ui
# http://0.0.0.0:8888
```