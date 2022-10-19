# Celery
- A specialized distributed task queue that simplify the management of task
- Task queue are used as a mechanism to distribute work across threads or machines.
- A task queue input is a unit of work called a task
- Dedicated worker processes constantly monitor task handles are common asynchornous
- As a task queueing system, Celery works well with long running processes or small repeatable tasks.
- The types of problems Celery handles are common asynchronous tasks.

# COMMUNICATION
- Celery communicates via messages, usually using broker to mediate between client and workers.
- To initiate a task the client adds message to the queue, and the brocker then deliver that message 
to a worker. 
- Redis and RabbitMQ are the brockers compeletely supported by Celery.
- RabbitMQ is the default message broker for Celery.

# Monitoring
- Flower is the real-time web application monitoring and admistration tool for Celery.

# Use CASES of Celery
- Sending out emails as Background tasks in an app
- Processing the uploaded images in the background
- Offline training of ML models
- Periodic tasks like report generation or web scrapping
