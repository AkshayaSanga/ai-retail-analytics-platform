#!/bin/bash

echo "Setting up AI Retail Analytics Platform..."

# Create directories
mkdir -p src/data tests config

# Create empty Python files
touch src/analytics.py
touch src/data/data_preprocessing.py
touch src/data/data_visualization.py
touch tests/test_analytics.py
touch tests/test_data_preprocessing.py

# Create requirements file
echo "numpy\npandas\nmatplotlib\nscikit-learn" > requirements.txt

# Create a config file
echo '{
  "data_source": "path/to/data",
  "model_params": {
      "n_estimators": 100,
      "max_depth": 5
  }
}' > config/config.json

echo "Project setup completed successfully!"