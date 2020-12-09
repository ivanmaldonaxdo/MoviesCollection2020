/*Insertar acá el código para Registrar el Service Worker*/
// Initialize the service worker
if ('serviceWorker' in navigator) {
    navigator.serviceWorker.register("{% url 'serviceworker' %}", {
        scope: '.' // <--- THIS BIT IS REQUIRED
    }).then(function (registration) {
        console.log('ServiceWorker registration successful with scope: ', registration.scope);
    }, function (err) {
        console.log('ServiceWorker registration failed: ', err);
    });
}
/*---------------------------------------------------------------*/
(function (i, s, o, g, r, a, m) {
    i['GoogleAnalyticsObject'] = r; i[r] = i[r] || function () {
        (i[r].q = i[r].q || []).push(arguments)
    }, i[r].l = 1 * new Date(); a = s.createElement(o),
        m = s.getElementsByTagName(o)[0]; a.async = 1; a.src = g; m.parentNode.insertBefore(a, m)
})(window, document, 'script', 'https://www.google-analytics.com/analytics.js', 'ga');

ga('create', 'UA-59325548-2', 'auto');
ga('send', 'pageview');
// src: url("../../templates/PeliSeries/sw.js");