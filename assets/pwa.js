/* Registers the MoneyBySharma service worker (sw.js). No install prompts. */
if ("serviceWorker" in navigator) addEventListener("load", function () { navigator.serviceWorker.register("/sw.js").catch(function () {}); });
