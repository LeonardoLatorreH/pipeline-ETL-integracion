import pandas as pd
import logging

logger = logging.getLogger(__name__)

def extract(raw_path: str) -> dict:
    """Lee los CSVs de Olist desde data/raw/ y retorna un diccionario de DataFrames."""

    logger.info("Iniciando extraccion de datos...")

    datasets = {
        "customers":   pd.read_csv(f"{raw_path}/olist_customers_dataset.csv"),
        "sellers":     pd.read_csv(f"{raw_path}/olist_sellers_dataset.csv"),
        "products":    pd.read_csv(f"{raw_path}/olist_products_dataset.csv"),
        "categories":  pd.read_csv(f"{raw_path}/product_category_name_translation.csv"),
        "orders":      pd.read_csv(f"{raw_path}/olist_orders_dataset.csv"),
        "order_items": pd.read_csv(f"{raw_path}/olist_order_items_dataset.csv"),
        "payments":    pd.read_csv(f"{raw_path}/olist_order_payments_dataset.csv"),
        "reviews":     pd.read_csv(f"{raw_path}/olist_order_reviews_dataset.csv"),
    }

    for name, df in datasets.items():
        logger.info(f"  {name}: {len(df):,} registros | {df.shape[1]} columnas")

    logger.info("Extraccion completada.")
    return datasets
