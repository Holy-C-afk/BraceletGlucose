import os
import subprocess
import sys

def run_command(command):
    print(f"Running: {command}")
    subprocess.run(command, shell=True, check=True)

def create_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created directory: {path}")

def main():
    # Create virtual environment
    run_command("python -m venv venv")
    
    # Activate virtual environment
    if sys.platform == "win32":
        activate_cmd = ".\\venv\\Scripts\\activate"
    else:
        activate_cmd = "source venv/bin/activate"
    
    # Install requirements
    run_command(f"{activate_cmd} && pip install -r requirements.txt")
    
    # Create Django project
    run_command(f"{activate_cmd} && django-admin startproject diabetes_bracelet .")
    
    # Create apps directory
    create_directory("apps")
    
    # Create Django apps
    apps = ["users", "devices", "metrics", "dashboard"]
    for app in apps:
        run_command(f"{activate_cmd} && python manage.py startapp {app} apps/{app}")
    
    # Create additional directories
    directories = [
        "static",
        "templates",
        "media",
        "docs"
    ]
    for directory in directories:
        create_directory(directory)
    
    print("\nProject setup completed successfully!")
    print("\nNext steps:")
    print("1. Activate the virtual environment:")
    print(f"   {activate_cmd}")
    print("2. Run migrations:")
    print("   python manage.py migrate")
    print("3. Create a superuser:")
    print("   python manage.py createsuperuser")
    print("4. Run the development server:")
    print("   python manage.py runserver")

if __name__ == "__main__":
    main() 