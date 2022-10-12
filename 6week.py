import psycopg2
users = [
    (1,"James",25,"male","USA"),
    (2,"Leila",32,"female","France"),
    (3,"Brigitte",35,"female","England"),
    (4,"Mike",40,"male","Denmark"),
    (5,"Elizabeth",21,"female","Canada"),
]
posts = [
    (1,"Happy","I am feeling very happy today",1),
    (2,"Hot Weather","The weather is very hot today",2),
    (3,"Help","I need some help with my work",2),
    (4,"Great News","I'm getting married",1),
    (5,"Interesting Game","It was a fantastic game of tennis",5),
    (6,"Party","Anyone up for a late-night party today?",3),
]
def createconnection(host,user,password,db_name):
    connection= None
    try:
        connection = psycopg2.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        user_records = ", ".join(["%s"] * len(users))
        post_records = ", ".join(["%s"] * len(posts))
        with connection.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL,
                age INTEGER,
                gender TEXT,
                nationality TEXT
                );
                CREATE TABLE IF NOT EXISTS posts(
                id INTEGER PRIMARY KEY ,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id)
                );
                CREATE TABLE IF NOT EXISTS comments (
                id INTEGER PRIMARY KEY ,
                text TEXT NOT NULL,
                user_id INTEGER NOT NULL,
                post_id INTEGER NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users(id),
                FOREIGN KEY (post_id) REFERENCES posts (id)
                );
                CREATE TABLE IF NOT EXISTS likes (
                id INTEGER PRIMARY KEY,
                user_id INTEGER NOT NULL,
                post_id integer NOT NULL,
                FOREIGN KEY (user_id) REFERENCES users (id),
                FOREIGN KEY (post_id) REFERENCES posts (id)
);
                SELECT * FROM users;
                """
            )
            # insert_query = (
            #     f"INSERT INTO users (id,name, age, gender, nationality) VALUES {user_records}"
            # )
            # cursor = connection.cursor()
            # cursor.execute(insert_query, users)
            # insert2_query = (
            #     f"INSERT INTO posts (id,title, description, user_id) VALUES {post_records}"
            # )
            # cursor.execute(insert2_query,posts)
            print(cursor.fetchall())
            connection.commit()
            connection.close()
    except Exception as ex:
        print("ERR with postgresql: ", ex)
connection = createconnection("127.0.0.1","postgres","1000","py")