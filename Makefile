# AgroDataZoom Makefile
# Automation for project setup and common tasks

.PHONY: help setup install clean test lint format notebook clean-notebooks

# Default target
help:
	@echo "🌾 AgroDataZoom - Global Agricultural Data Analysis"
	@echo "=================================================="
	@echo ""
	@echo "Available commands:"
	@echo "  setup          - Initial project setup"
	@echo "  install        - Install Python dependencies"
	@echo "  notebook       - Launch Jupyter notebook"
	@echo "  clean          - Clean temporary files"
	@echo "  clean-notebooks- Clear notebook outputs"
	@echo "  test           - Run tests (when available)"
	@echo "  lint           - Lint Python code"
	@echo "  format         - Format Python code"
	@echo ""

# Initial project setup
setup:
	@echo "🚀 Setting up AgroDataZoom project..."
	@python -m pip install --upgrade pip
	@pip install -r requirements.txt
	@echo "📁 Creating data directories..."
	@mkdir -p data/raw/turkey/tuik
	@mkdir -p data/processed
	@mkdir -p data/external
	@mkdir -p reports/figures
	@echo "✅ Setup completed!"

# Install dependencies
install:
	@echo "📦 Installing dependencies..."
	@pip install -r requirements.txt
	@echo "✅ Dependencies installed!"

# Launch Jupyter notebook
notebook:
	@echo "📚 Launching Jupyter notebook..."
	@jupyter notebook notebooks/

# Clean temporary files
clean:
	@echo "🧹 Cleaning temporary files..."
	@find . -type f -name "*.pyc" -delete
	@find . -type d -name "__pycache__" -delete
	@find . -type d -name ".pytest_cache" -delete
	@echo "✅ Cleanup completed!"

# Clear notebook outputs
clean-notebooks:
	@echo "📝 Clearing notebook outputs..."
	@jupyter nbconvert --clear-output --inplace notebooks/**/*.ipynb
	@echo "✅ Notebook outputs cleared!"

# Run tests (placeholder for future implementation)
test:
	@echo "🧪 Running tests..."
	@echo "📝 Tests not yet implemented. Add pytest configuration when ready."

# Lint Python code
lint:
	@echo "🔍 Linting Python code..."
	@echo "📝 Install flake8 or pylint for code linting"
	# @flake8 src/ --max-line-length=88

# Format Python code
format:
	@echo "🎨 Formatting Python code..."
	@echo "📝 Install black for code formatting"
	# @black src/
