// 白名单：只允许这些域名加载图片
const whitelist = [
    "52pojie.cn",
];

// 判断是否是白名单中的网址
function isWhitelisted(url) {
    try {
        const hostname = new URL(url).hostname;
        return whitelist.some(domain => hostname.endsWith(domain));
    } catch (e) {
        return false;
    }
}

// 拦截所有图片请求
browser.webRequest.onBeforeRequest.addListener(
    function (details) {
        if (!isWhitelisted(details.initiator || details.documentUrl || "")) {
            return { cancel: true }; // 阻止图片加载
        }
        return {}; // 允许加载
    },
    { urls: ["<all_urls>"], types: ["image"] },
    ["blocking"]
);