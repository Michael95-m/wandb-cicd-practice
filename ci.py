import wandb

print(f"Wandb version: {wandb.__version__}")
assert wandb.__version__ == "0.15.0", "Expected version 0.15.0 and the version didn't match"
