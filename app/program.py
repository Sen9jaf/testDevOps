from flask import Flask
import psycopg2
import redis

app = Flask(__name__)

@app.route('/')
def index():
    try:
        conn = psycopg2.connect(
            host='db',
            dbname='postgres',
            user='postgres',
            password='postgres'
        )
        r = redis.Redis(host='redis', port=6379)
        r.set('status', 'OK')
        redis_status = r.get('status').decode()
        return f'✅ DB Connected, 🔁 Redis: {redis_status}'
    except Exception as e:
        return f'❌ Error: {str(e)}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

