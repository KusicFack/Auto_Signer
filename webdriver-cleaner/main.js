delete window.navigator.wrappedJSObject.__proto__.webdriver;
console.log('navigator.webdriver cleaned:', window.navigator.wrappedJSObject.webdriver);