from datasets import load_dataset


data = load_dataset('super_glue', 'boolq', trust_remote_code=True)
print(data)
