```markdown
# Quick Start Guide

This document outlines the steps to get up and running with your setup.

## Step 1 - Start PostgreSQL Server

Use Docker Compose to start the PostgreSQL server. Run the following command:

```bash
docker-compose up -d
```

## Step 2 - Generate Data

You should run 01_explore notebook to generate the data. Here is how you can do that:

```bash
jupyter notebook notebooks/01_gen_data.ipynb
jupyter notebook notebooks/04_build_feature.ipynb
jupyter notebook notebooks/05_modeling.ipynb
```
Follow the steps in the notebook to generate the data.

## Step 3 - Setup Your Feature Store

Use make apply to tell the feature store to create the infra. You can do this by running the following command:

```bash
make apply
```

## Step 4 - Start Using 

After setting up your feature store, you can start using it. If you're not sure where to start, refer to our other guides and documentation.
```

```bash
make api
```