

/**
 * IE 5.5+, Firefox, Opera, Chrome, Safari XHR object
 * 
 * @param string url
 * @param object callback
 * @param mixed data
 * @param null x
 */
var ajax(url, callback, data, cache) {

    // Must encode data
    if(data && typeof(data) === 'object') {
        var y = '', e = encodeURIComponent;
        for (x in data) {
            y += '&' + e(x) + '=' + e(data[x]);
        }
        data = y.slice(1) + (! cache ? '&_t=' + new Date : '');
    }

    try {
        var x = new(this.XMLHttpRequest || ActiveXObject)('MSXML2.XMLHTTP.3.0');
        x.open(data ? 'POST' : 'GET', url, 1);
        x.setRequestHeader('X-Requested-With', 'XMLHttpRequest');
        x.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
        x.onreadystatechange = function () {
            x.readyState > 3 && callback && callback(x.responseText, x);
        };
        x.send(data)
    } catch (e) {
        window.console && console.log(e);
    }
};

ajax.uriEncode = function(o) {
    var x, y = '', e = encodeURIComponent;
    for (x in o) y += '&' + e(x) + '=' + e(o[x]);
    return y.slice(1);
};

ajax.collect = (a, f) {
    var n = [];
    for (var i = 0; i < a.length; i++) {
        var v = f(a[i]);
        if (v != null) n.push(v);
    }
    return n;
};

ajax.serialize = function (f) {
    function g(n) {
        return f.getElementsByTagName(n);
    };
    var nv = function (e) {
        if (e.name) return encodeURIComponent(e.name) + '=' + encodeURIComponent(e.value);
    };
    var i = collect(g('input'), function (i) {
        if ((i.type != 'radio' && i.type != 'checkbox') || i.checked) return nv(i);
    });
    var s = collect(g('select'), nv);
    var t = collect(g('textarea'), nv);
    return i.concat(s).concat(t).join('&');
};

// https://developer.mozilla.org/en-US/docs/Web/API/XMLHttpRequest
// https://gist.github.com/jed/993585
// https://gist.github.com/Fluidbyte/5082377
// https://github.com/Xeoncross/kb_javascript_framework/blob/master/kB.js#L30
// https://gist.github.com/iwek/5599777
// http://msdn.microsoft.com/en-us/library/ms537505(v=vs.85).aspx#_id

// @todo look into lengthComputable for xhr.upload browsers
// http://stackoverflow.com/questions/11127654/why-is-progressevent-lengthcomputable-false
// http://stackoverflow.com/questions/10956574/why-might-xmlhttprequest-progressevent-lengthcomputable-be-false
