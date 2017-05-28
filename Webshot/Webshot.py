from subprocess import Popen

class Webshot:
    _pagresPath = ""
    _imageSize = "1600x900"
    _delay = 2
    _crop = False
    _scale = 1
    _imageFormat = 'png'
    _url = ""
    _headers = ""
    _userAgent = "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36"


    def capture(self, url):
        print url
        if not isinstance(url, basestring):
            url = self.buildCommaSeperated(url)

        _commandArray = [self._pagresPath,  # File to Call
                         url,
                         self._imageSize,
                         "--delay={0}".format(self._delay),
                         "--format={0}".format(self._imageFormat),
                         "--scale={0}".format(self._scale),
                         "--user-agent={0}".format(self._userAgent)
                          ]
        print _commandArray
        Popen(_commandArray)

    def buildCommaSeperated(self, list):
        return " ".join(map(str, list))

    def buildHeaders(self, headers):
        _headers = ""
        if isinstance(headers, list):
            for header in headers:
                _headers += "--header={0} ".format(header)
        else:
            _headers = headers
        print _headers
        return _headers


    def configure(self, path, size=False, delay=False, crop=False, scale=False, imageFormat=False, userAgent=False, headers=False):
        self._pagresPath = path
        self._crop = "--crop" if crop else ""
        self._imageSize = self.buildCommaSeperated(size) if size else self._imageSize
        self._delay = delay if delay else self._delay
        self._scale = scale if scale else self._scale
        self._imageFormat = imageFormat if imageFormat else self._imageFormat
        self._userAgent = userAgent if userAgent else self._userAgent
        self._headers = self.buildHeaders(headers) if headers else ""


