## 1 Real Worl example: Multithreading for I/O bound task

## Scenario: Webscraping

web scraping often involves making numerous network requests to fetch web pages.
These tasks are I/O bound because they spent lot of time waiting for responses from servers.
Multithreading can significantly improve performance by allowing multiple pages to be fetched concurently.



## 2 Real Worl example: Multiprocessing for CPU bound tasks

## Scenario: Factorial Calculation

Factorial Calculation, especially for large numbers, involve significant computational work.
Multiprocessing can be used to distribute the workload across multiple CPU scores, improving performance.