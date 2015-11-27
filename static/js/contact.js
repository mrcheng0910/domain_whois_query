$(document).ready(function() {
//创建和初始化地图函数：
    function initMap() {
        createMap();//创建地图
        setMapEvent();//设置地图事件
        addMapControl();//向地图添加控件
        addMapOverlay();//向地图添加覆盖物
    }

    function createMap() {
        map = new BMap.Map("map");
        map.centerAndZoom(new BMap.Point(122.087905, 37.534715), 17);
    }

    function setMapEvent() {
        map.enableScrollWheelZoom();
        map.enableKeyboard();
        map.enableDragging();
        map.enableDoubleClickZoom()
    }

    function addClickHandler(target, window) {
        target.addEventListener("click", function () {
            target.openInfoWindow(window);
        });
    }

    function addMapOverlay() {
        var markers = [
            {
                content: "",
                title: "我的位置",
                imageOffset: {width: 0, height: -21},
                position: {lat: 37.533656, lng: 122.089037}
            }
        ];
        for (var index = 0; index < markers.length; index++) {
            var point = new BMap.Point(markers[index].position.lng, markers[index].position.lat);
            var marker = new BMap.Marker(point, {
                icon: new BMap.Icon("http://api.map.baidu.com/lbsapi/createmap/images/icon.png", new BMap.Size(20, 25), {
                    imageOffset: new BMap.Size(markers[index].imageOffset.width, markers[index].imageOffset.height)
                })
            });
            var label = new BMap.Label(markers[index].title, {offset: new BMap.Size(25, 5)});
            var opts = {
                width: 200,
                title: markers[index].title,
                enableMessage: false
            };
            var infoWindow = new BMap.InfoWindow(markers[index].content, opts);
            marker.setLabel(label);
            addClickHandler(marker, infoWindow);
            map.addOverlay(marker);
        }
        ;
    }

    //向地图添加控件
    function addMapControl() {
        var navControl = new BMap.NavigationControl({anchor: BMAP_ANCHOR_TOP_LEFT, type: 3});
        map.addControl(navControl);
    }
    var map;
    initMap();
});

$(document).ready(function(){
    //导航栏定位
    $("#contact").attr("class","active");
});