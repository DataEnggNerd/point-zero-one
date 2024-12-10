# Backend communication design patterns

This area explains on the common and different designs adopted to communicate between different services, frontend-to-backend, microservices etc.

## Request response model

Classic
clints sends request to backend, backend responds
how backend understands/parse the requests - beginning to ending
cost of parsing a request is not cheap
server -> parse >> process >> responds
parsing 
    - serialisation and deserialisation
    - parsing xml > json > protobuf
Where is this used
    - web, DNS, SSH
    - RPC
    - SQL
    - API (SOAP/ REST/ GraphQL)

Structure of request
GET (method) /(path) HTTP1.1(protocol)
Headers 
<CRLF>
BODY

Where it is not useful
- Notifications (where backend have info)
- Chat system
- Long requests (High time taking)

Request-response travel
Client 
- Create request (t0)
Server
- Receive and parse (t2) - network and parsing(serialisation and deserialisation) takes time
- Process the request (t10) - CPU bound actions or anything
- Prepare response (t11)
Client 
- Receive and process response (t13)
  
## Synchronous and Asynchronous

Can I do work while I am waiting for other response?

Synchronouse 
- Blocking
- Sequential
- Caller and Receiver are in sync
- Example in OS - read data from disk

Asynchronous
- Caller sends requests and do other stuff while waiting
- caller gets status update by different methods
  - Callback
  - Poll
  - Spawn new thread that waits

Synchronicity is client property
Async implementations in other paradigms
- in programming implemented with promises and futures
- Queued backend processing - Celery in Python
- Async commits in PostgreSQL
  - uses .wal to stage commits and flushes (memory to disk)
- Asynchronous replication in databases
- Asynchronous IO in linux (epoll, io_uring)

## Push

- Immediate / On demand response 
- Real time notifications
- Server proactively sends response to client
- Response without request to a webhook
- Realtime, Unidirectional transport
- Use cases 
  - user notification
  - chat messages
  - 
Cons
- Client has to be online
- Client needs to implemented with handling methodology
- Client need to have capacity to handle

## Polling

### Short Polling 
- Short polling in general
- Part of asynchronous implementation to check result of a promise/future
- Sort of opposite to Push, clients polls(checks) server for update/status/message
- Not a single req-res, but a set of req-res calls between client and server

- Sequence of actions
  - Client --Is A ready?--> Server => NO
  - Client --Is A ready?--> Server => NO
  - Client --Is A ready?--> Server => NO
  - Client --Is A ready?--> Server => Yes! Here is your response

Cons 
- Too much of traffic (chatty) with increasing number of clients
- High network bandwidth
- Wasted backend resources, server need to check the status and respond

### Long polling
- Avoid chattiness of short polling
- Once status fails, server stops responding and proactively notifies when the status changes
- Kafka uses this pattern

Cons 
- Not real time
  
## Server sent events
- Designed for HTTP
- One request and long, unending, realtime response
- Responses sents as chunks from server to client
- Streaming of data from server to client
Events
- Client sends a request with special header
- Server sends long set of events from server
- Server doesn't end the response

Cons
- Client has to be online always
- Client may not be able to handle the response
- HTTP/1.1 have limitation in this (6 connection problem - need to study)

## Publish Subscribe
- One publisher, many readers
- Base for microservices, where a request has to be used/consumbe by multiple services
- Youtube upload service is best example where multiple heavy actions has to be done for same data
- Overcomes coupling and sequential actions in microservices

Pros 
- Scalability
- Decoupling and no dependancy between workers
  
Cons
- Message delivery issues, Celery ghost tasks
- Broker level issue of network saturation
- 