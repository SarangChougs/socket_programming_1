  window.mwPerformance=(window.performance&&performance.mark)?performance:{mark:function(){}};window.mwNow=(function(){var perf=window.performance,navStart=perf&&perf.timing&&perf.timing.navigationStart;return navStart&&typeof perf.now==='function'?function(){return navStart+perf.now();}:function(){return Date.now();};}());window.isCompatible=function(str){var ua=str||navigator.userAgent;return!!((function(){'use strict';return!this&&!!Function.prototype.bind&&!!window.JSON;}())&&'querySelector'in document&&'localStorage'in window&&'addEventListener'in window&&!(ua.match(/webOS\/1\.[0-4]|SymbianOS|Series60|NetFront|Opera Mini|S40OviBrowser|MeeGo|Android.+Glass|^Mozilla\/5\.0 .+ Gecko\/$|googleweblight/)||ua.match(/PlayStation/i)));};(function(){var NORLQ,script;if(!isCompatible()){document.documentElement.className=document.documentElement.className.replace(/(^|\s)client-js(\s|$)/,'$1client-nojs$2');NORLQ=window.NORLQ||[];while(NORLQ.length){NORLQ.shift()();}window.NORLQ={push:function(
fn){fn();}};window.RLQ={push:function(){}};return;}function startUp(){mw.config=new mw.Map(true);mw.loader.addSource({"local":"/dftwiki/load.php"});mw.loader.register([["site","12marf6",[1]],["site.styles","0itcr6t",[],"site"],["noscript","0ysu2cn",[],"noscript"],["filepage","1mzzc5o"],["user.groups","1hekr4e",[5]],["user","0olh7fm",[6],"user"],["user.styles","0n5gazc",[],"user"],["user.defaults","19q17n2"],["user.options","0bhc5ha",[7],"private"],["user.tokens","0jugyyq",[],"private"],["mediawiki.language.data","14i3h1c",[176]],["mediawiki.skinning.elements","0b0vzur"],["mediawiki.skinning.content","1e8z95n"],["mediawiki.skinning.interface","1xicy8d"],["mediawiki.skinning.content.parsoid","09z3zlg"],["mediawiki.skinning.content.externallinks","1u3bpet"],["jquery.accessKeyLabel","0lmb72e",[25,133]],["jquery.appear","1px437x"],["jquery.async","0d1hctd"],["jquery.autoEllipsis","1c1ompe",[37]],["jquery.badge","1inhxh3",[173]],["jquery.byteLength","0ihmyk6"],["jquery.byteLimit","0ukjpy8",[
21]],["jquery.checkboxShiftClick","11idn8z"],["jquery.chosen","0awx64b"],["jquery.client","131n0z6"],["jquery.color","0gebmfl",[27]],["jquery.colorUtil","1spphau"],["jquery.confirmable","1qwe3eb",[177]],["jquery.cookie","1a53uwq"],["jquery.expandableField","1btn3so"],["jquery.farbtastic","0kqfpij",[27]],["jquery.footHovzer","1f0afvm"],["jquery.form","17a6lu7"],["jquery.fullscreen","0hkq3vb"],["jquery.getAttrs","0yi2ibc"],["jquery.hidpi","1bj27es"],["jquery.highlightText","0abhr6w",[133]],["jquery.hoverIntent","1vvk0zd"],["jquery.i18n","0z9wm8w",[175]],["jquery.localize","0eq50kc"],["jquery.makeCollapsible","13kgbfs"],["jquery.mockjax","1pzjjdu"],["jquery.mw-jump","0y2u1o0"],["jquery.placeholder","1s1cd24"],["jquery.qunit","0fb70jm"],["jquery.spinner","1jtkabb"],["jquery.jStorage","1n39js7"],["jquery.suggestions","1dakeyo",[37]],["jquery.tabIndex","1c8gz8l"],["jquery.tablesorter","19anq5l",[133,178]],["jquery.textSelection","1ks276h",[25]],["jquery.throttle-debounce","12obsdq"],[
"jquery.xmldom","06lv5bl"],["jquery.tipsy","0d6swwj"],["jquery.ui.core","11htrhr",[56],"jquery.ui"],["jquery.ui.core.styles","0yf9825",[],"jquery.ui"],["jquery.ui.accordion","1jjv8xa",[55,75],"jquery.ui"],["jquery.ui.autocomplete","15cx39z",[64],"jquery.ui"],["jquery.ui.button","06wbq6u",[55,75],"jquery.ui"],["jquery.ui.datepicker","006vs4d",[55],"jquery.ui"],["jquery.ui.dialog","1afgdbm",[59,62,66,68],"jquery.ui"],["jquery.ui.draggable","16kj6nc",[55,65],"jquery.ui"],["jquery.ui.droppable","0e675it",[62],"jquery.ui"],["jquery.ui.menu","1pis9lw",[55,66,75],"jquery.ui"],["jquery.ui.mouse","1p2y0lo",[75],"jquery.ui"],["jquery.ui.position","15sxehp",[],"jquery.ui"],["jquery.ui.progressbar","0cb1j8i",[55,75],"jquery.ui"],["jquery.ui.resizable","0y95idr",[55,65],"jquery.ui"],["jquery.ui.selectable","0sl2f5g",[55,65],"jquery.ui"],["jquery.ui.slider","1nki6g8",[55,65],"jquery.ui"],["jquery.ui.sortable","1uylk6s",[55,65],"jquery.ui"],["jquery.ui.spinner","1ugax48",[59],"jquery.ui"],[
"jquery.ui.tabs","019g4cr",[55,75],"jquery.ui"],["jquery.ui.tooltip","193e2er",[55,66,75],"jquery.ui"],["jquery.ui.widget","06b2l7w",[],"jquery.ui"],["jquery.effects.core","1e7gv6n",[],"jquery.ui"],["jquery.effects.blind","0vz56iu",[76],"jquery.ui"],["jquery.effects.bounce","001p79m",[76],"jquery.ui"],["jquery.effects.clip","1r6hrs3",[76],"jquery.ui"],["jquery.effects.drop","014veo3",[76],"jquery.ui"],["jquery.effects.explode","1grvo1o",[76],"jquery.ui"],["jquery.effects.fade","0c5iobe",[76],"jquery.ui"],["jquery.effects.fold","06an212",[76],"jquery.ui"],["jquery.effects.highlight","0z7b0bc",[76],"jquery.ui"],["jquery.effects.pulsate","1l8efts",[76],"jquery.ui"],["jquery.effects.scale","0llvsoo",[76],"jquery.ui"],["jquery.effects.shake","1yzc1cr",[76],"jquery.ui"],["jquery.effects.slide","03l0dro",[76],"jquery.ui"],["jquery.effects.transfer","0xd773m",[76],"jquery.ui"],["json","1hekr4e"],["moment","0g3fng0",[173]],["mediawiki.apihelp","1gbnxmz"],["mediawiki.template","1huj5ub"],[
"mediawiki.template.mustache","0ovm4bb",[93]],["mediawiki.template.regexp","1wvj7wt",[93]],["mediawiki.apipretty","0jf1xzd"],["mediawiki.api","0yo1rxg",[150,9]],["mediawiki.api.category","0gne0di",[138,97]],["mediawiki.api.edit","0f3j6wg",[138,148]],["mediawiki.api.login","0z9uloy",[97]],["mediawiki.api.options","00y8mas",[97]],["mediawiki.api.parse","094ofg6",[97]],["mediawiki.api.upload","006ir50",[99]],["mediawiki.api.user","1c18rg4",[97]],["mediawiki.api.watch","010w4tx",[97]],["mediawiki.api.messages","0hs4pmg",[97]],["mediawiki.api.rollback","1mmmwga",[97]],["mediawiki.content.json","06an10r"],["mediawiki.confirmCloseWindow","0x2ft0b"],["mediawiki.debug","1ackzvr",[32]],["mediawiki.diff.styles","09t9v3f"],["mediawiki.feedback","0muhz0w",[138,127,273]],["mediawiki.feedlink","0uyuh6k"],["mediawiki.filewarning","0a92xsi",[269]],["mediawiki.ForeignApi","0tauozs",[116]],["mediawiki.ForeignApi.core","052p6m8",[97,265]],["mediawiki.helplink","02n4bq6"],["mediawiki.hidpi","02bdr16",[36],
null,null,"return'srcset'in new Image();"],["mediawiki.hlist","0hr6mcl"],["mediawiki.htmlform","1xrhzbw",[22,133]],["mediawiki.htmlform.checker","1qwucgd",[52]],["mediawiki.htmlform.ooui","0b7atkx",[269]],["mediawiki.htmlform.styles","0fkkhbt"],["mediawiki.htmlform.ooui.styles","06s0qsc"],["mediawiki.icon","1xlem6t"],["mediawiki.inspect","13x664t",[21,133]],["mediawiki.messagePoster","1jlee2t",[115]],["mediawiki.messagePoster.wikitext","0tq65lq",[99,127]],["mediawiki.notification","0cd9i2o",[150]],["mediawiki.notify","0u8tsva"],["mediawiki.notification.convertmessagebox","0gsu1x3",[129]],["mediawiki.notification.convertmessagebox.styles","1r6la9w"],["mediawiki.RegExp","15jq2p2"],["mediawiki.pager.tablePager","1jzlukx"],["mediawiki.searchSuggest","0n9fcgw",[35,48,97]],["mediawiki.sectionAnchor","1wt966j"],["mediawiki.storage","0b1opbx"],["mediawiki.Title","1gagsn0",[21,150]],["mediawiki.Upload","0kq029a",[103]],["mediawiki.ForeignUpload","0j58a3k",[115,139]],[
"mediawiki.ForeignStructuredUpload.config","0msydx9"],["mediawiki.ForeignStructuredUpload","1okni25",[141,140]],["mediawiki.Upload.Dialog","0pptklb",[144]],["mediawiki.Upload.BookletLayout","1rcel80",[139,177,262,91,271,273]],["mediawiki.ForeignStructuredUpload.BookletLayout","0bd5iwm",[142,144,106,181,254,249]],["mediawiki.toc","0he5oje",[154]],["mediawiki.Uri","1a0zw1x",[150,95]],["mediawiki.user","1vzw7v8",[104,137,8]],["mediawiki.userSuggest","0dafk79",[48,97]],["mediawiki.util","0153wcw",[16,130]],["mediawiki.viewport","1fq3d1p"],["mediawiki.checkboxtoggle","1g6d5z7"],["mediawiki.checkboxtoggle.styles","1l6t65n"],["mediawiki.cookie","0axqqzw",[29]],["mediawiki.toolbar","0x88vbv",[51]],["mediawiki.experiments","0aq65yx"],["mediawiki.action.edit","0c2ssj0",[51,158,97,251]],["mediawiki.action.edit.styles","05mo206"],["mediawiki.action.edit.collapsibleFooter","0j7ymr9",[41,125,137]],["mediawiki.action.edit.preview","0xd1n0v",[33,46,51,97,111,177,269]],["mediawiki.action.history",
"0i83fyw"],["mediawiki.action.history.styles","0q0kii4"],["mediawiki.action.history.diff","09t9v3f"],["mediawiki.action.view.dblClickEdit","15yz4e7",[150,8]],["mediawiki.action.view.metadata","1tdgsyp"],["mediawiki.action.view.categoryPage.styles","0t2e1zn"],["mediawiki.action.view.postEdit","14owfca",[177,129]],["mediawiki.action.view.redirect","02b6ddn",[25]],["mediawiki.action.view.redirectPage","10vamv6"],["mediawiki.action.view.rightClickEdit","0y5mseb"],["mediawiki.action.edit.editWarning","12p8eys",[51,109,177]],["mediawiki.action.view.filepage","0f31p67"],["mediawiki.language","024c5ll",[174,10]],["mediawiki.cldr","0e0yolj",[175]],["mediawiki.libs.pluralruleparser","0dsmsbx"],["mediawiki.language.init","0ntwujo"],["mediawiki.jqueryMsg","1uce3ei",[173,150,8]],["mediawiki.language.months","1jal6jv",[173]],["mediawiki.language.names","02wxp1n",[176]],["mediawiki.language.specialCharacters","0qem0v5",[173]],["mediawiki.libs.jpegmeta","0x8skki"],["mediawiki.page.gallery","0m816ef",[
52,183]],["mediawiki.page.gallery.styles","1reejtf"],["mediawiki.page.gallery.slideshow","01egyjr",[138,97,271,286]],["mediawiki.page.ready","0mikueq",[16,23,43]],["mediawiki.page.startup","0dz4k0l"],["mediawiki.page.patrol.ajax","0yhrp6r",[46,138,97]],["mediawiki.page.watch.ajax","0op18qk",[138,105,177,186]],["mediawiki.page.rollback","1vns91h",[46,107]],["mediawiki.page.image.pagination","1jtjjsp",[46,150]],["mediawiki.rcfilters.filters.base.styles","1xcn413"],["mediawiki.rcfilters.highlightCircles.seenunseen.styles","07ouq3y"],["mediawiki.rcfilters.filters.dm","0h6algw",[21,147,101,148,265]],["mediawiki.rcfilters.filters.ui","1dza0w6",[41,193,268,280,282,284,286]],["mediawiki.special","0tokyyb"],["mediawiki.special.apisandbox.styles","0mzll89"],["mediawiki.special.apisandbox","0wzkynq",[41,97,177,252,268]],["mediawiki.special.block","1wri8kl",[120,150]],["mediawiki.special.changecredentials.js","1uaotii",[97,122]],["mediawiki.special.changeslist","1wc1bua"],[
"mediawiki.special.changeslist.enhanced","1v633xp"],["mediawiki.special.changeslist.legend","181e2e5"],["mediawiki.special.changeslist.legend.js","0d5t030",[41,154]],["mediawiki.special.changeslist.visitedstatus","0u4pg6t"],["mediawiki.special.comparepages.styles","0w1oro6"],["mediawiki.special.contributions","0suz7sz",[177,249]],["mediawiki.special.edittags","0n3nb0f",[24]],["mediawiki.special.edittags.styles","0vxlulz"],["mediawiki.special.import","06bzmmu"],["mediawiki.special.movePage","003ee2u",[247,251]],["mediawiki.special.movePage.styles","1ts6v1v"],["mediawiki.special.pageLanguage","062vnwn",[269]],["mediawiki.special.pagesWithProp","1mlov6w"],["mediawiki.special.preferences","04e3apd",[109,173,131]],["mediawiki.special.preferences.styles","1jncndn"],["mediawiki.special.recentchanges","1uzmwp4"],["mediawiki.special.search","16k5wdg",[260]],["mediawiki.special.search.commonsInterwikiWidget","0ds7aut",[147,97,177]],["mediawiki.special.search.interwikiwidget.styles","1jedace"],[
"mediawiki.special.search.styles","12u6ni3"],["mediawiki.special.undelete","0slljko"],["mediawiki.special.unwatchedPages","178tkrs",[138,105]],["mediawiki.special.upload","047ldrg",[46,138,97,109,177,181,224,93]],["mediawiki.special.upload.styles","1nondqn"],["mediawiki.special.userlogin.common.styles","0kyfkdw"],["mediawiki.special.userlogin.login.styles","17kykt9"],["mediawiki.special.userlogin.signup.js","1hhijzy",[97,121,177]],["mediawiki.special.userlogin.signup.styles","0mocfy8"],["mediawiki.special.userrights","123eklo",[131]],["mediawiki.special.watchlist","17ft2c2",[138,105,177,269]],["mediawiki.special.watchlist.styles","1yfc9x8"],["mediawiki.special.version","0cwiwij"],["mediawiki.legacy.config","1v7jw8h"],["mediawiki.legacy.commonPrint","13da7zq"],["mediawiki.legacy.protect","1kslxek",[22]],["mediawiki.legacy.shared","0uzhozb"],["mediawiki.legacy.oldshared","1ef2xww"],["mediawiki.legacy.wikibits","00ev435"],["mediawiki.ui","0u9e3d5"],["mediawiki.ui.checkbox","0i8zbc0"],[
"mediawiki.ui.radio","1wnbuvq"],["mediawiki.ui.anchor","1apgqep"],["mediawiki.ui.button","0mnvt86"],["mediawiki.ui.input","045tnyj"],["mediawiki.ui.icon","1r53gvt"],["mediawiki.ui.text","0y85y2q"],["mediawiki.widgets","0a6v3ug",[22,37,138,97,248,271]],["mediawiki.widgets.styles","1l7f5hh"],["mediawiki.widgets.DateInputWidget","1vb4n0o",[250,91,271]],["mediawiki.widgets.DateInputWidget.styles","18ep7re"],["mediawiki.widgets.visibleByteLimit","1xuoxh9",[22,269]],["mediawiki.widgets.datetime","0w37x9k",[269,287,288]],["mediawiki.widgets.CategorySelector","1hekr4e",[254]],["mediawiki.widgets.CategoryMultiselectWidget","0im428d",[115,138,271]],["mediawiki.widgets.SelectWithInputWidget","1twqrow",[256,271]],["mediawiki.widgets.SelectWithInputWidget.styles","04l1zjz"],["mediawiki.widgets.MediaSearch","0zr0hly",[115,138,271]],["mediawiki.widgets.UserInputWidget","0i3w1my",[97,271]],["mediawiki.widgets.UsersMultiselectWidget","1aenaf9",[97,271]],["mediawiki.widgets.SearchInputWidget","06fn0l6",
[135,247]],["mediawiki.widgets.SearchInputWidget.styles","0p9c3i3"],["mediawiki.widgets.StashedFileWidget","0hf4065",[97,269]],["es5-shim","1hekr4e"],["dom-level2-shim","1hekr4e"],["oojs","0ycfhqk"],["mediawiki.router","1i5l60v",[267]],["oojs-router","1d2qx9j",[265]],["oojs-ui","1hekr4e",[272,271,273]],["oojs-ui-core","015a6cz",[173,265,270,277,278,283,274,275]],["oojs-ui-core.styles","15m6znx"],["oojs-ui-widgets","1o67wgs",[269,279,287,288]],["oojs-ui-toolbars","0fov2jh",[269,288]],["oojs-ui-windows","0ojm5o7",[269,288]],["oojs-ui.styles.indicators","1tphh15"],["oojs-ui.styles.textures","0xjhi5t"],["oojs-ui.styles.icons-accessibility","05lcnl8"],["oojs-ui.styles.icons-alerts","03a43va"],["oojs-ui.styles.icons-content","1y0im0r"],["oojs-ui.styles.icons-editing-advanced","1jvkl5l"],["oojs-ui.styles.icons-editing-core","02th4rz"],["oojs-ui.styles.icons-editing-list","0zgtit4"],["oojs-ui.styles.icons-editing-styling","0zqqgzj"],["oojs-ui.styles.icons-interactions","07io994"],[
"oojs-ui.styles.icons-layout","1clh4ac"],["oojs-ui.styles.icons-location","1vfzpvn"],["oojs-ui.styles.icons-media","15lbs60"],["oojs-ui.styles.icons-moderation","0ceqb25"],["oojs-ui.styles.icons-movement","1sjv89r"],["oojs-ui.styles.icons-user","1ffbarj"],["oojs-ui.styles.icons-wikimedia","0317e1d"],["skins.cologneblue","065f70d"],["skins.modern","0sr9r11"],["skins.monobook.styles","0eyhnkd"],["skins.vector.styles","1o2ncdn"],["skins.vector.styles.experimental.print","1xaqe0n"],["skins.vector.styles.responsive","18ad5ar"],["skins.vector.js","0eoai8v",[49,52]],["ext.cite.styles","0ppdok2"],["ext.cite.a11y","1y8sr56"],["ext.cite.style","03jefc0"],["ext.pygments","1fdinex"],["jquery.wikiEditor","1hekr4e",[304],"ext.wikiEditor"],["jquery.wikiEditor.core","1064vw1",[51,173],"ext.wikiEditor"],["jquery.wikiEditor.dialogs","0z7njg1",[49,61,308],"ext.wikiEditor"],["jquery.wikiEditor.dialogs.config","1hdrg2v",[48,304,145,143,93],"ext.wikiEditor"],["jquery.wikiEditor.preview","05ubijs",[303,97],
"ext.wikiEditor"],["jquery.wikiEditor.publish","1hvjd1p",[304],"ext.wikiEditor"],["jquery.wikiEditor.toolbar","16m525w",[18,29,303,310],"ext.wikiEditor"],["jquery.wikiEditor.toolbar.config","194hmwh",[308,180],"ext.wikiEditor"],["jquery.wikiEditor.toolbar.i18n","1rlpdev",[],"ext.wikiEditor"],["ext.wikiEditor","1hekr4e",[314],"ext.wikiEditor"],["ext.wikiEditor.styles","0dhpuc5",[],"ext.wikiEditor"],["ext.wikiEditor.core","0r6lw4w",[303,148],"ext.wikiEditor"],["ext.wikiEditor.dialogs","022d8g3",[317,305],"ext.wikiEditor"],["ext.wikiEditor.preview","058pfpc",[313,306],"ext.wikiEditor"],["ext.wikiEditor.publish","0ecvu95",[313,307],"ext.wikiEditor"],["ext.wikiEditor.toolbar","1s7ynkf",[313,309],"ext.wikiEditor"],["ext.bootstrap.styles","04ptzi6"],["ext.bootstrap.scripts","0mjoul1"],["ext.bootstrap","1hekr4e",[319,318]],["skin.chameleon.jquery-sticky","15tdttt",[],"skin.chameleon"]]);;mw.config.set({"wgLoadScript":"/dftwiki/load.php","debug":!1,"skin":"vector","stylepath":
"/dftwiki/skins","wgUrlProtocols":"bitcoin\\:|ftp\\:\\/\\/|ftps\\:\\/\\/|geo\\:|git\\:\\/\\/|gopher\\:\\/\\/|http\\:\\/\\/|https\\:\\/\\/|irc\\:\\/\\/|ircs\\:\\/\\/|magnet\\:|mailto\\:|mms\\:\\/\\/|news\\:|nntp\\:\\/\\/|redis\\:\\/\\/|sftp\\:\\/\\/|sip\\:|sips\\:|sms\\:|ssh\\:\\/\\/|svn\\:\\/\\/|tel\\:|telnet\\:\\/\\/|urn\\:|worldwind\\:\\/\\/|xmpp\\:|\\/\\/","wgArticlePath":"/dftwiki/index.php/$1","wgScriptPath":"/dftwiki","wgScriptExtension":".php","wgScript":"/dftwiki/index.php","wgSearchType":null,"wgVariantArticlePath":!1,"wgActionPaths":{},"wgServer":"http://www.science.smith.edu","wgServerName":"www.science.smith.edu","wgUserLanguage":"en","wgContentLanguage":"en","wgTranslateNumerals":!0,"wgVersion":"1.30.0","wgEnableAPI":!0,"wgEnableWriteAPI":!0,"wgMainPageTitle":"Main Page","wgFormattedNamespaces":{"-2":"Media","-1":"Special","0":"","1":"Talk","2":"User","3":"User talk","4":"Dftwiki","5":"Dftwiki talk","6":"File","7":"File talk","8":"MediaWiki","9":"MediaWiki talk",
"10":"Template","11":"Template talk","12":"Help","13":"Help talk","14":"Category","15":"Category talk"},"wgNamespaceIds":{"media":-2,"special":-1,"":0,"talk":1,"user":2,"user_talk":3,"dftwiki":4,"dftwiki_talk":5,"file":6,"file_talk":7,"mediawiki":8,"mediawiki_talk":9,"template":10,"template_talk":11,"help":12,"help_talk":13,"category":14,"category_talk":15,"image":6,"image_talk":7,"project":4,"project_talk":5},"wgContentNamespaces":[0],"wgSiteName":"dftwiki","wgDBname":"dftwiki_new","wgExtraSignatureNamespaces":[],"wgAvailableSkins":{"cologneblue":"CologneBlue","modern":"Modern","monobook":"MonoBook","vector":"Vector","chameleon":"Chameleon","fallback":"Fallback","apioutput":"ApiOutput"},"wgExtensionAssetsPath":"/dftwiki/extensions","wgCookiePrefix":"dftwiki_new","wgCookieDomain":"","wgCookiePath":"/","wgCookieExpiration":2592000,"wgResourceLoaderMaxQueryLength":2000,"wgCaseSensitiveNamespaces":[],"wgLegalTitleChars":" %!\"$&'()*,\\-./0-9:;=?@A-Z\\\\\\^_`a-z~+\\u0080-\\uFFFF",
"wgIllegalFileChars":":/\\\\","wgResourceLoaderStorageVersion":1,"wgResourceLoaderStorageEnabled":!0,"wgForeignUploadTargets":["local"],"wgEnableUploads":!0,"wgCiteVisualEditorOtherGroup":!1,"wgCiteResponsiveReferences":!0,"wgWikiEditorMagicWords":{"redirect":"#REDIRECT","img_right":"right","img_left":"left","img_none":"none","img_center":"center","img_thumbnail":"thumb","img_framed":"frame","img_frameless":"frameless"},"mw.msg.wikieditor":"--~~~~"});var RLQ=window.RLQ||[];while(RLQ.length){RLQ.shift()();}window.RLQ={push:function(fn){fn();}};window.NORLQ={push:function(){}};}window.mediaWikiLoadStart=mwNow();mwPerformance.mark('mwLoadStart');script=document.createElement('script');script.src="/dftwiki/load.php?debug=false&lang=en&modules=jquery%2Cmediawiki&only=scripts&skin=vector&version=06tqsl3";script.onload=script.onreadystatechange=function(){if(!script.readyState||/loaded|complete/.test(script.readyState)){script.onload=script.onreadystatechange=null;script=null;startUp
();}};document.getElementsByTagName('head')[0].appendChild(script);}());
