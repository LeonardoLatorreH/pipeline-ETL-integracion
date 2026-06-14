import logging
import os
from dotenv import load_dotenv
from extract import extract
from transform import transform
from load import load

# -- configuracion de logs --
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler("logs/etl.log"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def main():
    load_dotenv()

    raw_path = "data/raw"

    connection_string = (
        f"mysql+pymysql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}"
        f"@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
    )

    logger.info("=" * 50)
    logger.info("PIPELINE ETL — Brazilian E-Commerce Olist")
    logger.info("=" * 50)

    datasets = extract(raw_path)
    datasets = transform(datasets)
    load(datasets, connection_string)

    logger.info("Pipeline completado exitosamente.")

if __name__ == "__main__":
    main()
