### example

##### Browser Headers

- https://http-support.vercel.app/generate-browser-headers?limit=

#### User Agent

- https://http-support.vercel.app/generate-user-agent?limit=

```javascript
const { data } = await axios.get(
  "https://http-support.vercel.app/generate-browser-headers?limit=10"
);

// response
// [
//   {
//     "Accept": "*/*",
//     "Connection": "keep-alive",
//     "User-Agent": "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.1805 Safari/537.36"
//   },
//   {
//     "Accept": "*/*",
//     "Connection": "keep-alive",
//     "User-Agent": "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770 Safari/537.36 OPR/57.0.3098.116"
//   }
// ]

const headers = data[0];
const url = "my_url";

const resWithBrowserHeaders = axios.get(url, {
  headers,
});
```
