# Caching
Caching is a great example of the ubiquitous time-space tradeoff in programming. You can save time by using space to store results.

In the case of websites, the browser can save a copy of images, stylesheets, javascript or the entire page. The next time the user needs that resource (such as a script or logo that appears on every page), the browser doesn’t have to download it again. Fewer downloads means a faster, happier site.

TASKS

[0-basic_cache.py](https://github.com/Mmaureeny/alx-backend/blob/0x01-caching/0-basic_cache.py)

Create a class BasicCache that inherits from BaseCaching and is a caching system:
