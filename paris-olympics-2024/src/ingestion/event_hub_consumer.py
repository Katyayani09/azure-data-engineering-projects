from azure.eventhub import EventHubConsumerClient

CONNECTION_STR = "YourEventHubConnectionString"
EVENT_HUB_NAME = "olympics-data"

def on_event(partition_context, event):
    print(f"Received data from partition {partition_context.partition_id}: {event.body_as_str()}")
    # Save or process the event data
    partition_context.update_checkpoint(event)

consumer = EventHubConsumerClient.from_connection_string(
    CONNECTION_STR,
    consumer_group="$Default",
    eventhub_name=EVENT_HUB_NAME,
)

try:
    with consumer:
        consumer.receive(on_event=on_event, starting_position="-1")
except KeyboardInterrupt:
    print("Stopped receiving events.")
finally:
    consumer.close()