import pika
import json
import sys
import time

RABBITMQ_HOST = "localhost"


def start_consumer(user_id: str):
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host=RABBITMQ_HOST)
    )
    channel = connection.channel()

    queue_name = f"user_{user_id}_queue"
    channel.queue_declare(queue=queue_name, durable=True)

    def callback(ch, method, properties, body):
        message = json.loads(body)
        print(f"[Consumer - User {user_id}] Recebido: {message}")
        time.sleep(1)  # simula processamento
        print(f"[Consumer - User {user_id}] Processado ✅")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    print(f"[Consumer - User {user_id}] Aguardando mensagens...")
    channel.start_consuming()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Uso: python main.py <user_id>")
        sys.exit(1)

    user_id = sys.argv[1]
    start_consumer(user_id)
