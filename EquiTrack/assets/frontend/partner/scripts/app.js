!function(n){"use strict";var e=n.querySelector("#app");e.baseUrl="/",""!==window.location.port&&"8099"!==window.location.port||(e.baseUrl="/partners/"),e.appData={baseUrl:e.baseUrl,baseSite:window.location.origin,logoutEndpoint:window.location.origin+"/accounts/logout/",userInfoEp:window.location.origin+"/users/api/profile/",userPropertiesEp:window.location.origin+"/partnership/partnerstaffmember/",interventionsEp:[window.location.origin,"partners","api","interventions"].join("/")+"/",newIndicatorReportEp:window.location.origin+"/partners/api/indicatorreport/new/",getEndpoint:{userProperties:function(n){return[window.location.origin,"partners","api","profile",n].join("/")+"/"},interventionDetails:function(n){return[window.location.origin,"partners","api","interventions",n].join("/")+"/"},resultChainDetails:function(n){return[window.location.origin,"partners","api","resultchain",n].join("/")+"/"}},permissions:{partnerOnlyPermissions:["interventionsMenu","userInfoMenu"],defaultPermissions:["userInfoMenu"],partnerPermissions:["interventionsMenu"],managementPermissions:["statsMenu"]}},e.displayInstalledToast=function(){Polymer.dom(n).querySelector("platinum-sw-cache").disabled||Polymer.dom(n).querySelector("#caching-complete").show()},e.addEventListener("dom-change",function(){console.log("Our app is ready to rock!")}),window.addEventListener("WebComponentsReady",function(){}),window.addEventListener("paper-header-transform",function(e){var o=Polymer.dom(n).querySelector("#mainToolbar .app-name"),r=Polymer.dom(n).querySelector("#mainToolbar .middle-container"),i=Polymer.dom(n).querySelector("#mainToolbar .bottom-container"),t=e.detail,a=t.height-t.condensedHeight,s=Math.min(1,t.y/a),l=.5,c=a-t.y,p=a/(1-l),d=Math.max(l,c/p+l),u=1-s;Polymer.Base.transform("translate3d(0,"+100*s+"%,0)",r),Polymer.Base.transform("scale("+u+") translateZ(0)",i),Polymer.Base.transform("scale("+d+") translateZ(0)",o)}),e.scrollPageToTop=function(){e.$.headerPanelMain.scrollToTop(!0)},e.closeDrawer=function(){e.$.paperDrawerPanel.closeDrawer()}}(document);