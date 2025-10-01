from fastapi import FastAPI
import pika
import json

app = FastAPI()

RABBITMQ_HOST = "localhost"  # ou "rabbitmq" no docker-compose


def publish_message(user_id: str, message: dict):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST)
    )
    channel = connection.channel()

    # Cada usuário tem sua própria fila
    queue_name = f"user_{user_id}_queue"
    channel.queue_declare(queue=queue_name, durable=True)

    channel.basic_publish(
        exchange="",
        routing_key=queue_name,
        body=json.dumps(message),
        properties=pika.BasicProperties(
            delivery_mode=2  # mensagem persistente
        )
    )
    connection.close()


@app.post("/notify/{user_id}")
def notify_user(user_id: str, payload: dict):
    publish_message(user_id, payload)
    return {"status": f"Notificação enviada para usuário {user_id}", "payload": payload}
