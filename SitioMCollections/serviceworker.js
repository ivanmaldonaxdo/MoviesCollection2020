// Base Service Worker implementation.  To use your own Service Worker, set the PWA_SERVICE_WORKER_PATH variable in settings.py

var staticCacheName = "django-pwa-v" + new Date().getTime();
var filesToCache = [

    '/offline/',
    '/static/css/bootstrap.css',
    '/static/css/estilos.css',
    '/static/css/style.css',
    '/static/css/fontawesome.css',
    '/static/fonts/FuentesWeb.ttf?k04a4h',
    '/static/js/funciones.js',
    '/media/images/carousel/Peliculas/StarWars_sl_3V2pvZH.jpg',
    '/media/images/carousel/Peliculas/iron_man_3_sl_EsVKJqb.jpg',
    '/media/images/carousel/Series/breaking_bad_sl_rwONbcF.jpg',
    '/static/js/bootstrap.js',
    '/static/img/photo.png',
    '/static/img/fondo-2.jpg',
    '/static/img/index_1.jpg',
    '/static/fonts/Roboto-Light.ttf',
    '/static/fonts/Woodland.ttf',
    '/static/img/Formulario_2.png',
    '/static/img/LogoWeb MovieCollection(Header).png',


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

self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request)
            .then(response => {
                return response || fetch(event.request);
            })
            .catch(() => {
                return caches.match('/offline/');
            })
    )
});

//Cache dinamico - Se guarda el cache de cada template que visite el cliete


// self.addEventListener("fetch", function(event) {
//     event.respondWith(
//         fetch(event.request)
//         .then(function(result){
//             return caches.open(staticCacheName)
//             .then(function(c){
//                 c.put(event.request.url, result.clone())
//                 return result;
//             })
//         })
//         .catch(function(e){
//             return caches.match(event.request);
//         })
//     )

// });
