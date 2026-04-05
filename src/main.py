"""Main entry point for AI Retail Analytics Platform"""
import logging
from config.logging_config import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

def main():
    """Main application function"""
    logger.info("Starting AI Retail Analytics Platform")
    print("\n✅ AI Retail Analytics Platform initialized!")
    print("📂 Project structure created")
    print("🚀 Ready for development\n")

if __name__ == "__main__":
    main()
