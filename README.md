# ReadableStream support for Encoding
Human-readable patch to the [Encoding Standard]
(http://encoding.spec.whatwg.org) to add support for [ReadableStream]
(http://streams.spec.whatwg.org).

To see the HTML rendered as HTML, go to
http://htmlpreview.github.io/?https://github.com/ricea/encoding-streams/blob/master/patch.html

This enables uses like

```javascript
fetch(url)
  .then(response => {
    let stringStream = response.body.pipeThough(new TextDecoder());
    // stringStream is now a stream of strings.
  });
```

The Bikeshed source for these changes can be found at
https://github.com/ricea/encoding/blob/stream-support/encoding.bs.
