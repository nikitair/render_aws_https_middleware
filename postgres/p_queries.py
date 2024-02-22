from p_connector import postgres_connector



@postgres_connector
def demo_query(connector, id):
    cursor = connector.cursor()
    query = f"SELECT * FROM statistics.market_leader_polygons WHERE id = {id}"

    cursor.execute(query)

    data = cursor.fetchall()

    return data


if __name__ == "__main__":
    print(demo_query(1))