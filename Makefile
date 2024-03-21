.PHONY = apply

apply:
	export PYTHONPATH=. \
	&& export REGISTRY_PATH="$(realpath .)/registry.pb" \
	&& export FEATURE_FOLDER_PATH="$(realpath .)/features" \
	&& python feature_repo/store.py

ui:
	feast ui