from p_connector import postgres_connector



@postgres_connector
def demo_query(connector, id):
    cursor = connector.cursor()
    query = f"SELECT * FROM statistics.market_leader_polygons WHERE id = %s"

    cursor.execute(query, str(id))

    data = cursor.fetchall()

    return data


# @postgres_connector
# def create_dragontail_cookies_table(connector):
#     cursor = connector.cursor()
#     cursor.execute("""
#                    CREATE TABLE cookies.dragontail_cookies
#                    (
#                     id BIGSERIAL PRIMARY KEY,
#                     user_agent VARCHAR(255),
#                     url_path VARCHAR(255),
#                     ip VARCHAR(255),
#                     network VARCHAR(255),
#                     city VARCHAR(255),
#                     region VARCHAR(255),
#                     region_code VARCHAR(255),
#                     country VARCHAR(255),
#                     country_name VARCHAR(255),
#                     country_code VARCHAR(255),
#                     country_code_iso3 VARCHAR(255),
#                     country_capital VARCHAR(255),
#                     country_tld VARCHAR(255),
#                     continent_code VARCHAR(255),
#                     in_eu INT DEFAULT 0,
#                     postal VARCHAR(255),
#                     latitude VARCHAR(255),
#                     longitude VARCHAR(255),
#                     timezone VARCHAR(255),
#                     utc_offset VARCHAR(255),
#                     country_calling_code VARCHAR(255),
#                     currency VARCHAR(255),
#                     currency_name VARCHAR(255),
#                     languages VARCHAR(255),
#                     country_area INT,
#                     country_population INT,
#                     asn VARCHAR(255),
#                     org VARCHAR(255),
#                     _ga VARCHAR(255),
#                     language VARCHAR(255),
#                     cookieSettings VARCHAR(255),
#                     _ga_WFTDQVD03N VARCHAR(255),
#                     raw_data JSONB,
#                     created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
#                    );
#                    """)
#     print("table created")



if __name__ == "__main__":
    # print(demo_query(1))
    # create_dragontail_cookies_table()
    ...
