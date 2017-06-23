    var imagenes=new Array(
        '../sws/1.jpg',
        '../sws/2.jpg',
        '../sws/3.jpg',
        '../sws/4.jpg'
    );
    function rotarImagenes(){
        var index=Math.floor((Math.random()*imagenes.length));
        document.getElementById("imagen").src=imagenes[index];
    }
    onload=function(){
        rotarImagenes();
        setInterval(rotarImagenes,10000);
    }