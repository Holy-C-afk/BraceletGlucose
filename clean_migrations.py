import os

project_root = os.getcwd()

for root, dirs, files in os.walk(project_root):
    if 'migrations' in root:
        for file in files:
            if (file.endswith('.py') and file != '__init__.py') or file.endswith('.pyc'):
                file_path = os.path.join(root, file)
                try:
                    os.remove(file_path)
                    print(f"Deleted: {file_path}")
                except Exception as e:
                    print(f"Failed to delete {file_path}: {e}")

print("✅ Cleanup complete!")
