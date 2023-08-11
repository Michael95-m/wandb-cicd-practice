import wandb

print(f"Wandb version: {wandb.__version__}")
assert wandb.__version__ == "0.15.0", "Expected version didn't match"
