import argparse
import asyncio
import logging

from .service import run_etl_pipeline


def configure_logging():
    logging.basicConfig(
        level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s"
    )


def main():
    configure_logging()
    parser = argparse.ArgumentParser(description="ETL-Service-Pipeline CLI")
    parser.add_argument("--db", default="etl_service.db")
    parser.add_argument("urls", nargs="+", help="List of source URLs to extract from")
    args = parser.parse_args()
    asyncio.run(run_etl_pipeline(args.urls, args.db))


if __name__ == "__main__":
    main()
