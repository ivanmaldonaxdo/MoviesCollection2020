// Base Service Worker implementation.  To use your own Service Worker, set the PWA_SERVICE_WORKER_PATH variable in settings.py

var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [


    '/offline/',	
    '/',
    '/BiblioPelis/',
    '/BiblioSeries/',
    '/detail/2/',
    '/detail/3/',
    '/detail/4/',
    '/detail/5/',	
    '/media/images/Series/breaking_bad_Xxe5yJv.jpg',
    '/media/images/Series/malcom_el_del_medio_.jpg',
    '/media/images/Peliculas/iron_man_3_MEe5gaa.jpg',
    '/media/images/Peliculas/star_wars_Q8mHNVo.jpg',
    '/static/fonts/Woodland.ttf',
    '/media/images/carousel/Peliculas/StarWars_sl_3V2pvZH.jpg',
    '/media/images/carousel/Peliculas/iron_man_3_sl_EsVKJqb.jpg',
    '/media/images/carousel/Series/breaking_bad_sl_rwONbcF.jpg',
    '/static/css/bootstrap.css',
    '/static/css/estilos.css',
    '/static/css/style.css',
    '/static/fonts/FuentesWeb.ttf?k04a4h',
    '/static/fonts/Nunito-Light.ttf',
    '/static/fonts/Roboto-Light.ttf',
    '/static/img/Formulario_2.png',
    '/static/img/LogoWeb%20MovieCollection(Header).png',
    '/static/img/fondo-2.jpg',
    '/static/img/index_1.jpg',
    '/static/img/photo.png',
    '/static/js/bootstrap.js',
    '/static/js/funciones.js',
    '/static/js/jquery-3.3.1.js',


];

// Cache on install
self.addEventListener("install", event => {
    this.skipWaiting();
    event.waitUntil(
        caches.open(staticCacheName)
            .then(cache => {
                return cache.addAll(filesToCache);
            })
    )
});

// Clear cache on activate
self.addEventListener('activate', event => {
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames
                    .filter(cacheName => (cacheName.startsWith("django-pwa-")))
                    .filter(cacheName => (cacheName !== staticCacheName))
                    .map(cacheName => caches.delete(cacheName))
            );
        })
    );
});


// Serve from Cache

/*self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('/offline/');
            })
    )
});*/

//Cache dinamico - Se guarda el cache de cada template que visite el cliete

self.addEventListener("fetch", function(event) {
    event.respondWith(
        fetch(event.request)
        .then(function(result){
            return caches.open(staticCacheName)
            .then(function(c){
                c.put(event.request.url, result.clone())
                return result;
            })
        })
        .catch(function(e){
            return caches.match(event.request);
        })
    )
});
