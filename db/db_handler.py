import sqlite3
import json

def create_table_cookies_dragontail():
    conn = sqlite3.connect('dragontail.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS cookies (
                    id INTEGER PRIMARY KEY,
                    user_agent TEXT NOT NULL,
                    url_path TEXT NOT NULL,
                    ip TEXT NOT NULL,
                    network TEXT,
                    city TEXT,
                    region TEXT,
                    region_code TEXT,
                    country TEXT,
                    country_name TEXT,
                    country_code TEXT,
                    country_code_iso3 TEXT,
                    country_capital TEXT,
                    country_tld TEXT,
                    continent_code TEXT,
                    in_eu BOOLEAN,
                    postal TEXT,
                    latitude REAL,
                    longitude REAL,
                    timezone TEXT,
                    utc_offset TEXT,
                    country_calling_code TEXT,
                    currency TEXT,
                    currency_name TEXT,
                    languages TEXT,
                    country_area INTEGER,
                    country_population INTEGER,
                    asn TEXT,
                    org TEXT,
                    _ga TEXT,
                    language TEXT,
                    cookieSettings TEXT,
                    _ga_WFTDQVD03N TEXT,
                    raw_data JSON,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                  )''')

    conn.commit()
    conn.close()
    return True


def insert_cookies_data_dragontail(data_dict):
    try:
        conn = sqlite3.connect('dragontail.db')
        cursor = conn.cursor()

        user_agent = data_dict.get('user_agent', '')
        url_path = data_dict.get('url_path', '')
        cookies_result = data_dict.get('cookiesResult', {})
        ip_info_result = data_dict.get('ipInfoResult', {})

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

        raw_data = json.dumps(data_dict)

        cursor.execute('''INSERT INTO cookies (
                            user_agent, url_path,
                            ip, network, city, region, region_code,
                            country, country_name, country_code, country_code_iso3, country_capital, country_tld,
                            continent_code, in_eu, postal, latitude, longitude,
                            timezone, utc_offset, country_calling_code, currency,
                            currency_name, languages, country_area, country_population, asn, org,
                            _ga, language, cookieSettings, _ga_WFTDQVD03N, raw_data
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                        (user_agent, url_path,
                        ip, network, city, region, region_code,
                        country, country_name, country_code, country_code_iso3, country_capital, country_tld,
                        continent_code, in_eu, postal, latitude, longitude,
                        timezone, utc_offset, country_calling_code, currency,
                        currency_name, languages, country_area, country_population, asn, org,
                        _ga, language, cookie_settings, _ga_WFTDQVD03N, raw_data))

        conn.commit()
        conn.close()

        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
    

# -----------------------------------------
    
def create_table_cookies_fatalist():
    conn = sqlite3.connect('dragontail.db')
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS fatalist_cookies (
                    id INTEGER PRIMARY KEY,
                    user_agent TEXT NOT NULL,
                    url_path TEXT NOT NULL,
                    ip TEXT NOT NULL,
                    network TEXT,
                    city TEXT,
                    region TEXT,
                    region_code TEXT,
                    country TEXT,
                    country_name TEXT,
                    country_code TEXT,
                    country_code_iso3 TEXT,
                    country_capital TEXT,
                    country_tld TEXT,
                    continent_code TEXT,
                    in_eu BOOLEAN,
                    postal TEXT,
                    latitude REAL,
                    longitude REAL,
                    timezone TEXT,
                    utc_offset TEXT,
                    country_calling_code TEXT,
                    currency TEXT,
                    currency_name TEXT,
                    languages TEXT,
                    country_area INTEGER,
                    country_population INTEGER,
                    asn TEXT,
                    org TEXT,
                    _ga TEXT,
                    language TEXT,
                    cookieSettings TEXT,
                    _ga_WFTDQVD03N TEXT,
                    raw_data JSON,
                    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
                  )''')

    conn.commit()
    conn.close()
    return True


def insert_cookies_data_fatalist(data_dict):
    try:
        conn = sqlite3.connect('dragontail.db')
        cursor = conn.cursor()

        user_agent = data_dict.get('user_agent', '')
        url_path = data_dict.get('url_path', '')
        cookies_result = data_dict.get('cookiesResult', {})
        ip_info_result = data_dict.get('ipInfoResult', {})

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

        raw_data = json.dumps(data_dict)

        cursor.execute('''INSERT INTO fatalist_cookies (
                            user_agent, url_path,
                            ip, network, city, region, region_code,
                            country, country_name, country_code, country_code_iso3, country_capital, country_tld,
                            continent_code, in_eu, postal, latitude, longitude,
                            timezone, utc_offset, country_calling_code, currency,
                            currency_name, languages, country_area, country_population, asn, org,
                            _ga, language, cookieSettings, _ga_WFTDQVD03N, raw_data
                        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                        (user_agent, url_path,
                        ip, network, city, region, region_code,
                        country, country_name, country_code, country_code_iso3, country_capital, country_tld,
                        continent_code, in_eu, postal, latitude, longitude,
                        timezone, utc_offset, country_calling_code, currency,
                        currency_name, languages, country_area, country_population, asn, org,
                        _ga, language, cookie_settings, _ga_WFTDQVD03N, raw_data))

        conn.commit()
        conn.close()

        return True
    except Exception as e:
        print(f"Error occurred: {e}")
        return False
    


if __name__ == "__main__":
    ...