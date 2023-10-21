import csv

import numpy as np
import pandas as pd
from decouple import config

from app.core.database import SessionLocal
from app.models.geoname import GeoName

# Database configuration
DATABASE_URL = config("DATABASE_URL")

# TSV file path
tsv_file = "data.tsv"


def insert_data_from_tsv():
    df = pd.read_csv(tsv_file, sep="\t", quoting=csv.QUOTE_NONE)

    session = SessionLocal()

    try:
        for index, row in df.iterrows():
            row = row.replace(np.nan, None, regex=True)
            data = {
                "geoname_id": row["id"],
                "name": row["name"],
                "asciiname": row["ascii"],
                "alternatenames": row["alt_name"],
                "latitude": row["lat"],
                "longitude": row["long"],
                "feature_class": row["feat_class"],
                "feature_code": row["feat_code"],
                "country_code": row["country"],
                "cc2": row["cc2"],
                "admin1_code": row["admin1"],
                "admin2_code": row["admin2"],
                "admin3_code": row["admin3"],
                "admin4_code": row["admin4"],
                "population": row["population"],
                "elevation": row["elevation"],
                "dem": row["dem"],
                "timezone": row["tz"],
                "modification_date": row["modified_at"],
            }

            obj = GeoName(**data)
            session.add(obj)

        session.commit()

    except Exception as e:
        print(f"Error: {str(e)}")
        session.rollback()


insert_data_from_tsv()
