import json
from p_connector import postgres_connector
from logging_config import logger


@postgres_connector
def demo_query(connector, id: int):
    cursor = connector.cursor()
    query = "SELECT * FROM statistics.market_leader_polygons WHERE id = %s"
    cursor.execute(query, str(id))
    data = cursor.fetchall()

    return data


@postgres_connector
def get_all_data(connector):
    cursor = connector.cursor()
    query = "SELECT * FROM cookies.dragontail_cookies"
    cursor.execute(query)
    data = cursor.fetchall()

    return data


@postgres_connector
def insert_cookies_data_dragontail(connector, data: dict):
    cursor = connector.cursor()

    user_agent = data.get('user_agent', '')
    url_path = data.get('url_path', '')
    cookies_result = data.get('cookiesResult', {})
    ip_info_result = data.get('ipInfoResult', {})

    _ga = cookies_result.get('_ga', '')
    language = cookies_result.get('language', '')
    cookie_settings = cookies_result.get('cookieSettings', '')
    _ga_WFTDQVD03N = cookies_result.get('_ga_WFTDQVD03N', '')

    ip = ip_info_result.get('ip', '')
    network = ip_info_result.get('network', '')
    city = ip_info_result.get('city', '')
    region = ip_info_result.get('region', '')
    region_code = ip_info_result.get('region_code', '')
    country = ip_info_result.get('country', '')
    country_name = ip_info_result.get('country_name', '')
    country_code = ip_info_result.get('country_code', '')
    country_code_iso3 = ip_info_result.get('country_code_iso3', '')
    country_capital = ip_info_result.get('country_capital', '')
    country_tld = ip_info_result.get('country_tld', '')
    continent_code = ip_info_result.get('continent_code', '')
    in_eu = ip_info_result.get('in_eu', False)
    postal = ip_info_result.get('postal', '')
    latitude = ip_info_result.get('latitude', 0.0)
    longitude = ip_info_result.get('longitude', 0.0)
    timezone = ip_info_result.get('timezone', '')
    utc_offset = ip_info_result.get('utc_offset', '')
    country_calling_code = ip_info_result.get('country_calling_code', '')
    currency = ip_info_result.get('currency', '')
    currency_name = ip_info_result.get('currency_name', '')
    languages = ip_info_result.get('languages', '')
    country_area = ip_info_result.get('country_area', 0)
    country_population = ip_info_result.get('country_population', 0)
    asn = ip_info_result.get('asn', '')
    org = ip_info_result.get('org', '')
    raw_data = json.dumps(data)

    query = '''INSERT INTO cookies.dragontail_cookies (
                                user_agent, url_path,
                                ip, network, city, region, region_code,
                                country, country_name, country_code,
                                country_code_iso3, country_capital, country_tld,
                                continent_code, in_eu, postal, latitude, longitude,
                                timezone, utc_offset, country_calling_code,
                                currency, currency_name, languages, country_area,
                                country_population, asn, org, _ga, language,
                                cookieSettings, _ga_WFTDQVD03N, raw_data
                    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
                            %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

    cursor.execute(query, (user_agent, url_path, ip, network,
                   city, region, region_code, country, country_name,
                   country_code, country_code_iso3, country_capital,
                   country_tld, continent_code, in_eu, postal, latitude,
                   longitude, timezone, utc_offset, country_calling_code,
                   currency, currency_name, languages, country_area,
                   country_population, asn, org, _ga, language,
                   cookie_settings, _ga_WFTDQVD03N, raw_data))
    connector.commit()

    logger.info("DATA INSERTED IN TABLE "
                "cookies.dragontail_cookies SUCCESSFULLY")


@postgres_connector
def create_dragontail_cookies_table(connector):
    cursor = connector.cursor()
    cursor.execute("""
                   CREATE TABLE cookies.dragontail_cookies
                   (
                    id BIGSERIAL PRIMARY KEY,
                    user_agent VARCHAR(255),
                    url_path VARCHAR(255),
                    ip VARCHAR(255),
                    network VARCHAR(255),
                    city VARCHAR(255),
                    region VARCHAR(255),
                    region_code VARCHAR(255),
                    country VARCHAR(255),
                    country_name VARCHAR(255),
                    country_code VARCHAR(255),
                    country_code_iso3 VARCHAR(255),
                    country_capital VARCHAR(255),
                    country_tld VARCHAR(255),
                    continent_code VARCHAR(255),
                    in_eu BOOLEAN DEFAULT False,
                    postal VARCHAR(255),
                    latitude VARCHAR(255),
                    longitude VARCHAR(255),
                    timezone VARCHAR(255),
                    utc_offset VARCHAR(255),
                    country_calling_code VARCHAR(255),
                    currency VARCHAR(255),
                    currency_name VARCHAR(255),
                    languages VARCHAR(255),
                    country_area INT,
                    country_population INT,
                    asn VARCHAR(255),
                    org VARCHAR(255),
                    _ga VARCHAR(255),
                    language VARCHAR(255),
                    cookieSettings VARCHAR(255),
                    _ga_WFTDQVD03N VARCHAR(255),
                    raw_data JSONB,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                   );
                    """)
    print("table created")
