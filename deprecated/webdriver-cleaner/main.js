Object.defineProperty(Object.getPrototypeOf(navigator), 'webdriver', {
    get: () => undefined,
    configurable: true,
});
console.log('navigator.webdriver cleaned:', navigator.webdriver);