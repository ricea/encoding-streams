# ReadableStream support for Encoding
Human-readable patch to the [Encoding Standard](http://encoding.spec.whatwg.org)
to add support for [transform streams](http://streams.spec.whatwg.org/#ts-model).

To see the HTML rendered as HTML, go to
http://htmlpreview.github.io/?https://github.com/ricea/encoding-streams/blob/master/patch.html

This enables uses like

```javascript
const response = await fetch(url)
let stringStream = response.body.pipeThough(new TextDecoderStream());
```

The Bikeshed source for these changes can be found at
https://github.com/ricea/encoding/blob/stream-support/encoding.bs.
