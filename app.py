import psycopg2
from flask import Flask, request, jsonify,json
from config import config

app = Flask(__name__)

conn = None
cur=None
response=None

def connect():
    """ Connect to the PostgreSQL database server """
    
    try:
        # read connection parameters
        params = config()

        # connect to the PostgreSQL server
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)

        # create a cursor
        cur = conn.cursor()

        # execute a statement
        print('PostgreSQL database version:')
        cur.execute('SELECT version()')

        # display the PostgreSQL database server version
        db_version = cur.fetchone()
        print(db_version)

       
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    


@app.route('/login', methods=["POST"])
def login():
    connect()
    data = request.json
    
    cur.execute('SELECT name, phone, pass FROM public.users WHERE phone =? AND pass =?',data['phone'],data['pass'])
    columns = ('name', 'phone', 'pass')
    rows=cur.fetchone()

    if cur == None:
        results = []
        for row in rows:
            results.append(dict(zip(columns, row)))
        
        response = app.response_class(
                    response=json.dumps(results),
                    status=200,
                    mimetype='application/json'
                )
    else:
        response = app.response_class(
            response=json.dumps("{'status':'0'}"),
            status=200,
            mimetype='application/json'
        )

    print(results)
    return response


if __name__ == '__main__':
    app.run()
