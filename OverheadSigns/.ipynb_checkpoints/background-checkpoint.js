// Copyright (c) 2011 The Chromium Authors. All rights reserved.
// Use of this source code is governed by a BSD-style license that can be
// found in the LICENSE file.

// Called when the user clicks on the browser action.
// chrome.BrowserActions.onClicked.addListener(function(tab) {
// Customized to do be enabled no click needed
//chrome.tabs.onUpdated.addListener(function(tab) {
//    if (changeInfo.status == 'complete' && tab.active) {
//console.log("it worked")
//chrome.tabs.insertCSS({file:"styles.css"});
//    }
//});

function insertCSS() {
    var style = document.createElement('style');
    style.type = 'text/css';
    style.innerHTML = ".widget-image-header-close {visibility: hidden} .widget-image-header-scrim {visibility: hidden} .watermark { visibility: hidden;} .app-viewcard-strip {visibility: hidden} .scene-footer {visibility: hidden} #titlecard {visibility: hidden}";
    document.getElementsByTagName("head")[0].appendChild( style );
}