import wandb

print(f"Wandb version: {wandb.__version__}")
assert wandb.__version__ == "0.15.0", f"Expected version didn't match and the current version is {wandb.__version__}. Please fix the version"
