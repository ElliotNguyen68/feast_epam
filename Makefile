.PHONY = apply

apply:
	export PYTHONPATH=. && python feature_repo/store.py

ui:
	feast ui