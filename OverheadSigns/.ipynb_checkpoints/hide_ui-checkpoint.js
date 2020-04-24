// innerHTML is CSS to hide found in Google Streetview UI
var style = document.createElement("style");
style.type = "text/css";
style.innerHTML = ".widget-image-header-close {visibility: hidden} .widget-image-header-scrim {visibility: hidden} .watermark { visibility: hidden;} .app-viewcard-strip {visibility: hidden} .scene-footer {visibility: hidden} #titlecard {visibility: hidden}" 
document.getElementsByTagName('head')[0].appendChild(style);