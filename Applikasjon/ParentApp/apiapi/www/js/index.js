/*
 * Licensed to the Apache Software Foundation (ASF) under one
 * or more contributor license agreements.  See the NOTICE file
 * distributed with this work for additional information
 * regarding copyright ownership.  The ASF licenses this file
 * to you under the Apache License, Version 2.0 (the
 * "License"); you may not use this file except in compliance
 * with the License.  You may obtain a copy of the License at
 *
 * http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing,
 * software distributed under the License is distributed on an
 * "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
 * KIND, either express or implied.  See the License for the
 * specific language governing permissions and limitations
 * under the License.
 */
var app = {
    // Application Constructor
    initialize: function() {
        document.addEventListener('deviceready', this.onDeviceReady.bind(this), false);
    },

    // deviceready Event Handler
    //
    // Bind any cordova events here. Common events are:
    // 'pause', 'resume', etc.
    onDeviceReady: function() {
        this.receivedEvent('deviceready');
    },

    // Update DOM on a Received Event
    receivedEvent: function(id) {
        var parentElement = document.getElementById(id);
        var listeningElement = parentElement.querySelector('.listening');
        var receivedElement = parentElement.querySelector('.received');

        listeningElement.setAttribute('style', 'display:none;');
        receivedElement.setAttribute('style', 'display:block;');

        console.log('Received Event: ' + id);
    }
};
function setColor(e) {
    var target = e.target,
    count = +target.dataset.count;
    
    target.style.backgroundColor = count === 1 ? "#7FFF00" : '#FFFFFF';
    target.dataset.count = count === 1 ? 0 : 1;
    /*
     
     () : ? - this is conditional (ternary) operator - equals
     
     if (count === 1) {
     target.style.backgroundColor = "#7FFF00";
     target.dataset.count = 0;
     } else {
     target.style.backgroundColor = "#FFFFFF";
     target.dataset.count = 1;
     }
     target.dataset - return all "data attributes" for current element,
     in the form of object,
     and you don't need use global variable in order to save the state 0 or 1
     */ 
}

app.initialize();
