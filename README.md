# ReadableStream support for Encoding
Human-readable patch to the [Encoding Standard]
(http://encoding.spec.whatwg.org) to add support for [ReadableStream] (http://streams.spec.whatwg.org).

This enables uses like

```javascript
fetch(url)
  .then(response => {
    let stringStream = response.body.pipeThough(TextDecoder.stream());
    // stringStream is now a stream of strings.
  });
```
