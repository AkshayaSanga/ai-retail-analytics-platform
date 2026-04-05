#!/usr/bin/env python3
"""
AI Retail Analytics Platform - Automated Setup Script
This script creates the complete project structure and all necessary files.
"""

import os
import sys
from pathlib import Path

class ProjectSetup:
    def __init__(self, base_path="."):
        self.base_path = Path(base_path)
        self.created_items = []
        self.skipped_items = []

    def create_directory(self, dir_path):
        """Create a directory"""
        full_path = self.base_path / dir_path
        try:
            full_path.mkdir(parents=True, exist_ok=True)
            self.created_items.append(f"📁 {dir_path}")
            print(f"✓ Created directory: {dir_path}")
        except Exception as e:
            self.skipped_items.append(f"✗ {dir_path}")
            print(f"✗ Failed to create {dir_path}: {e}")

    def create_file(self, file_path, content):
        """Create a file with content"""
        full_path = self.base_path / file_path
        
        if full_path.exists():
            print(f"⊘ File already exists: {file_path}")
            return

        try:
            full_path.parent.mkdir(parents=True, exist_ok=True)
            with open(full_path, 'w', encoding='utf-8') as f:
                f.write(content)
            self.created_items.append(f"📄 {file_path}")
            print(f"✓ Created file: {file_path}")
        except Exception as e:
            print(f"✗ Failed to create {file_path}: {e}")

    def run_setup(self):
        """Execute the complete setup"""
        print("\n" + "="*70)
        print("🚀 AI RETAIL ANALYTICS PLATFORM - SETUP SCRIPT")
        print("="*70 + "\n")

        print("📁 Creating project directories...\n")
        self.setup_directories()

        print("\n📄 Creating Python modules...\n")
        self.setup_python_files()

        print("\n⚙️  Creating configuration files...\n")
        self.setup_config_files()

        print("\n🧪 Creating test files...\n")
        self.setup_test_files()

        print("\n📚 Creating documentation files...\n")
        self.setup_docs_and_config()

        self.print_summary()

    def setup_directories(self):
        """Create all required directories"""
        directories = [
            "src",
            "src/data_processing",
            "src/models",
            "src/database",
            "src/analytics",
            "config",
            "notebooks",
            "tests",
            "data/raw",
            "data/processed",
            "reports",
            "logs",
            "scripts",
            "models",
        ]
        
        for dir_path in directories:
            self.create_directory(dir_path)

    def setup_python_files(self):
        """Create all Python module files"""
        
        # Init files
        init_files = [
            "src/__init__.py",
            "src/data_processing/__init__.py",
            "src/models/__init__.py",
            "src/database/__init__.py",
            "src/analytics/__init__.py",
            "tests/__init__.py",
        ]
        
        for init_file in init_files:
            self.create_file(init_file, '"""Package initialization."""\n')

        # Main entry point
        self.create_file("src/main.py", '''"""Main entry point for AI Retail Analytics Platform"""
import logging
from config.logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def main():
    """Main application function"""
    logger.info("Starting AI Retail Analytics Platform")
    print("\\n✅ AI Retail Analytics Platform initialized!")
    print("📂 Project structure created")
    print("🚀 Ready for development\\n")

if __name__ == "__main__":
    main()
''')

    def setup_config_files(self):
        """Create configuration files"""
        
        # Config YAML
        self.create_file("config/config.yaml", '''# AI Retail Analytics Platform Configuration

database:
  host: localhost
  port: 5432
  name: retail_analytics
  user: postgres
  password: ${DB_PASSWORD}

data:
  raw_data_path: data/raw/
  processed_data_path: data/processed/

models:
  sales_predictor:
    type: random_forest
    n_estimators: 100
''')

        # Logging Config
        self.create_file("config/logging_config.py", '''"""Logging Configuration"""
import logging
from pathlib import Path

def setup_logging(log_level=logging.INFO):
    """Setup logging configuration"""
    
    log_dir = Path('logs')
    log_dir.mkdir(exist_ok=True)
    
    logger = logging.getLogger()
    logger.setLevel(log_level)
    
    # Remove existing handlers
    for handler in logger.handlers[:]:
        logger.removeHandler(handler)
    
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    
    # File handler
    file_handler = logging.FileHandler('logs/retail_analytics.log')
    file_handler.setFormatter(formatter)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    return logger
''')

    def setup_test_files(self):
        """Create test files"""
        
        self.create_file("tests/test_main.py", '''"""Unit tests for main application"""
import pytest

class TestMain:
    def test_placeholder(self):
        """Placeholder test"""
        assert True
''')

    def setup_docs_and_config(self):
        """Create documentation and configuration files"""
        
        # Requirements
        self.create_file("requirements.txt", '''# Core Libraries
pandas==2.0.3
numpy==1.24.3
python-dotenv==1.0.0

# Database
psycopg2-binary==2.9.6
sqlalchemy==2.0.19

# Machine Learning
scikit-learn==1.2.2
xgboost==1.7.5
lightgbm==4.0.0

# Visualization
matplotlib==3.7.1
seaborn==0.12.2
plotly==5.14.0

# Testing
pytest==7.4.0
pytest-cov==4.1.0

# Code Quality
black==23.7.0
flake8==6.0.0
pylint==2.17.5
''')

        # .env.example
        self.create_file(".env.example", '''# Database Configuration
DB_HOST=localhost
DB_PORT=5432
DB_NAME=retail_analytics
DB_USER=postgres
DB_PASSWORD=your_password

# Data Paths
DATA_RAW_PATH=data/raw/
DATA_PROCESSED_PATH=data/processed/

# Logging
LOG_LEVEL=INFO
''')

        # .gitignore
        self.create_file(".gitignore", '''# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
dist/
*.egg-info/

# Virtual Environment
venv/
ENV/
env/

# IDE
.vscode/
.idea/
*.swp

# Environment
.env

# Logs
logs/
*.log

# Data
data/raw/*
!data/raw/.gitkeep
data/processed/*
!data/processed/.gitkeep

# Models
models/*.pkl

# Reports
reports/*
!reports/.gitkeep

# Jupyter
.ipynb_checkpoints/

# OS
.DS_Store
Thumbs.db
''')

        # Gitkeep files
        self.create_file("data/raw/.gitkeep", "")
        self.create_file("data/processed/.gitkeep", "")
        self.create_file("reports/.gitkeep", "")
        self.create_file("logs/.gitkeep", "")

    def print_summary(self):
        """Print setup summary"""
        print("\n" + "="*70)
        print("✅ SETUP COMPLETE!")
        print("="*70)
        print(f"\n📊 Summary:")
        print(f"   Created: {len(self.created_items)} items")
        print(f"\n🚀 NEXT STEPS:")
        print("   1. python -m pip install --upgrade pip")
        print("   2. pip install -r requirements.txt")
        print("   3. cp .env.example .env  (or copy .env.example .env on Windows)")
        print("   4. git init")
        print("   5. git add .")
        print("   6. git commit -m 'Initial commit: AI Retail Analytics Platform'")
        print("   7. git remote add origin https://github.com/AkshayaSanga/ai-retail-analytics-platform.git")
        print("   8. git branch -M main")
        print("   9. git push -u origin main")
        print("\n" + "="*70)

if __name__ == "__main__":
    setup = ProjectSetup()
    setup.run_setup()