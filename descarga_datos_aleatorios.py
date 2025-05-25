import csv
import os
import time
import requests
import random

api_key = "XXXXX"



def read_cursor_from_csv(query, csv_file):
    """
    Lee el último cursor guardado en el archivo CSV para la query dada.
    
    Args:
        query (str): La consulta de búsqueda.
        csv_file (str): El archivo CSV donde se guarda el último cursor.
        
    Returns:
        str: El cursor almacenado, o None si no existe.
    """
    if os.path.exists(csv_file):
        with open(csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                if row['query'] == query:
                    return row['cursor']
    return None

def write_cursor_to_csv(query, cursor, csv_file):
    """
    Guarda o actualiza el cursor en el archivo CSV para la query dada.
    
    Args:
        query (str): La consulta de búsqueda.
        cursor (str): El cursor a guardar.
        csv_file (str): El archivo CSV donde se guarda el cursor.
    """
    rows = []

    # Leer el archivo si ya existe
    if os.path.exists(csv_file):
        with open(csv_file, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            rows = list(reader)

        # Eliminar cualquier fila con la misma query (para evitar duplicados)
        rows = [row for row in rows if row['query'] != query]

    # Añadir el nuevo cursor para la query
    rows.append({'query': query, 'cursor': cursor})

    # Sobrescribir el archivo con las filas actualizadas
    with open(csv_file, 'w', newline='', encoding='utf-8') as f:
        fieldnames = ['query', 'cursor']
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # Escribir el encabezado solo una vez
        writer.writeheader()

        # Escribir las filas
        writer.writerows(rows)


def fetch_twitter_data(query, cursor=None, max_retries=3, retry_delay=5):
    """
    Fetch data from Twitter API with pagination support
    
    Args:
        query (str): Search query
        cursor (str, optional): Pagination cursor, default is None
        max_retries (int): Maximum number of retry attempts
        retry_delay (int): Delay between retries in seconds
    
    Returns:
        dict: Data returned from the API
    """
    url = 'https://api.twitterapi.io/twitter/tweet/advanced_search'
    headers = {
        'x-api-key': api_key
    }

    params = {
        'query': query,
        "queryType": "Latest"
    }

    if cursor and cursor != 'null':
        params['cursor'] = cursor

    for attempt in range(max_retries):
        try:
            response = requests.get(url, headers=headers, params=params)
            response.raise_for_status()  # Raises HTTPError for bad status codes
            #print(response.json())
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Request error (attempt {attempt+1}/{max_retries}): {e}")
            if attempt < max_retries - 1:
                print(f"Waiting {retry_delay} seconds before retrying...")
                time.sleep(retry_delay)
            else:
                print("Maximum retry attempts reached, giving up")
                raise

def fetch_all_tweets(query, max_pages=None, csv_file='cursor_data.csv'):
    """
    Get all tweets matching the query, handling pagination and saving cursor
    
    Args:
        query (str): Search query
        max_pages (int, optional): Maximum number of pages to fetch, None means fetch all
        csv_file (str): The CSV file to store and read the cursor
        
    Returns:
        list: All tweets retrieved
    """
    all_tweets = []
    
    # Read the last cursor from CSV file
    cursor = read_cursor_from_csv(query, csv_file)
    #print(cursor)

    page_count = 0

    print(f"Starting to fetch tweets for query: '{query}'")

    while True:
        page_count += 1
        if max_pages and page_count > max_pages:
            print(f"Reached maximum page limit ({max_pages})")
            break

        print(f"Fetching page {page_count}, cursor: {cursor}")

        try:
            data = fetch_twitter_data(query, cursor)

            # Extract tweets
            if 'tweets' in data and data['tweets']:
                tweets_in_page = data['tweets']
                all_tweets.extend(tweets_in_page)
                print(f"Retrieved {len(tweets_in_page)} tweets in this page")
                json_to_csv(tweets_in_page, 'espanol_api.csv')
                # Save the last cursor to CSV
            else:
                print("No tweets found in this page")

            # Check if there's a next page
            if data.get('has_next_page') and data.get('next_cursor'):
                cursor = data['next_cursor']
                print(f"Found next page, cursor: {cursor}")
                time.sleep(1)  # Add delay to avoid too frequent requests
                write_cursor_to_csv(query, cursor, csv_file)
            else:
                print("No more pages")
                write_cursor_to_csv(query, "TERMINADO"+cursor, csv_file)
                break

        except Exception as e:
            print(f"Error while fetching tweets: {e}")
            break

    print(f"Total tweets retrieved: {len(all_tweets)}")


    return all_tweets

def json_to_csv(tweet_data, csv_file):
    """Convierte una lista de tweets en formato JSON a un archivo CSV y agrega los datos al archivo existente."""
    if isinstance(tweet_data, dict) and "tweets" in tweet_data:
        tweet_data = tweet_data["tweets"]  # Extraer la lista de tweets si está dentro de un diccionario

    # Definir los nombres de las columnas
    fieldnames = [
        'id', 'url', 'text', 'createdAt', 'source', 'lang', 'retweetCount', 'replyCount',
        'likeCount', 'quoteCount', 'viewCount', 'bookmarkCount', 'isReply', 
        'conversationId', 'inReplyToId', 'inReplyToUserId', 'inReplyToUsername',
        'author_id', 'author_username', 'author_name', 'author_verified', 'author_blue_verified',
        'author_followers', 'author_following', 'author_tweets', 'author_description',
        'author_location', 'author_createdAt', 'author_profilePicture', 'author_coverPicture',
        'media_urls', 'hashtags', 'user_mentions', 'author_isAutomated', 'author_fastFollowersCount',
        'author_favouritesCount', 'author_hasCustomTimelines', 'author_statusesCount', 'author_profile_bio',
        'place_id', 'place_type', 'place_full_name', 'place_country_code', 'place_country'
    ]

    # Escribir en el archivo CSV (en modo 'a' para agregar los datos)
    with open(csv_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)

        # Escribir el encabezado solo si el archivo está vacío
        if f.tell() == 0:
            writer.writeheader()

        for tweet in tweet_data:
            author = tweet.get('author', {})  # Información del autor
            place = tweet.get('place', {})
            media_urls = []
            if 'extendedEntities' in tweet and 'media' in tweet['extendedEntities']:
                media_urls = [m.get('media_url_https', '') for m in tweet['extendedEntities']['media']]

            hashtags = [h.get('text', '') for h in tweet.get('entities', {}).get('hashtags', [])]
            user_mentions = [um.get('screen_name', '') for um in tweet.get('entities', {}).get('user_mentions', [])]

            # Escapar comillas, saltos de línea y comas en los campos de texto
            def escape_text(text):
                if isinstance(text, str):  # Verificar si es una cadena de texto
                    text = text.replace('"', '""')  # Doble comilla para escapar las comillas
                    text = text.replace("\n", " ")  # Reemplazar saltos de línea por un espacio
                    text = text.replace("\r", "")  # Eliminar saltos de línea adicionales
                return text

            writer.writerow({
                'id': tweet.get('id'),
                'url': tweet.get('url'),
                'text': escape_text(tweet.get('text', '')),
                'createdAt': tweet.get('createdAt'),
                'source': tweet.get('source'),
                'lang': tweet.get('lang'),
                'retweetCount': tweet.get('retweetCount', 0),
                'replyCount': tweet.get('replyCount', 0),
                'likeCount': tweet.get('likeCount', 0),
                'quoteCount': tweet.get('quoteCount', 0),
                'viewCount': tweet.get('viewCount', 0),
                'bookmarkCount': tweet.get('bookmarkCount', 0),
                'isReply': tweet.get('isReply', False),
                'conversationId': tweet.get('conversationId'),
                'inReplyToId': tweet.get('inReplyToId'),
                'inReplyToUserId': tweet.get('inReplyToUserId'),
                'inReplyToUsername': tweet.get('inReplyToUsername'),
                'author_id': author.get('id'),
                'author_username': author.get('userName'),
                'author_name': author.get('name'),
                'author_verified': author.get('isVerified', False),
                'author_blue_verified': author.get('isBlueVerified', False),
                'author_followers': author.get('followers', 0),
                'author_following': author.get('following', 0),
                'author_tweets': author.get('statusesCount', 0),
                'author_description': escape_text(author.get('description', '')),
                'author_location': escape_text(author.get('location', '')),
                'author_createdAt': author.get('createdAt', ''),
                'author_profilePicture': author.get('profilePicture', ''),
                'author_coverPicture': author.get('coverPicture', ''),
                'media_urls': "; ".join(media_urls),
                'hashtags': "; ".join(hashtags),
                'user_mentions': "; ".join(user_mentions),
                'author_isAutomated': author.get('isAutomated', False),
                'author_fastFollowersCount': author.get('fastFollowersCount', 0),
                'author_favouritesCount': author.get('favouritesCount', 0),
                'author_hasCustomTimelines': author.get('hasCustomTimelines', False),
                'author_statusesCount': author.get('statusesCount', 0),
                'author_profile_bio': escape_text(author.get('profile_bio', '')),
                'place_id': place.get('id', 0),
                'place_type': place.get('place_type', 0),
                'place_full_name': escape_text(place.get('full_name', '')),
                'place_country_code': place.get('country_code', 0),
                'place_country': place.get('country', 0)
            })


# automatizamos las solicitudes
# para cada hora tomamos todos los tuits de un minuto random
for hora in range(0,24):
    minuto = random.randint(1, 59)
    minuto_prev = (minuto-1)%60
    segundo = random.randint(0, 59)
    # para seguir el formato que nos piden desde la API
    if minuto < 10:
        minuto = f"0{minuto}"
    # tambien hay que poner minuto prev en el formato correcto
    if minuto_prev < 10:
            minuto_prev = f"0{minuto_prev}"
    if segundo < 10:
        segundo = f"0{segundo}"
    for year in range(2015, 2025):
        search_query = f"(ser OR todos OR algo) lang:es until:{year}-06-28_{hora}:{minuto}:{segundo}_UTC since:{year}-06-28_{hora}:{minuto_prev}:{segundo}_UTC"  # Replace with your search query
        tweets = fetch_all_tweets(search_query, max_pages=100)  # Limit to 5 pages, set to None for all pages


# Llamar a la función con la variable `tweets`
#json_to_csv(tweets, 'orgullo_2017_bueno.csv')

print("CSV generado exitosamente: tweets_data.csv")

#print(tweets)